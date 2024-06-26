while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate danger check
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    # Airway Management
    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
    elif events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
        print(31)  # UseYankeurSuctionCatheter
    elif (
        events[7] > 0.1 or events[8] > 0.1 or events[9] > 0.1
    ):  # Severe Breathing issues
        print(29)  # Use Bag Valve Mask

    # Breathing management
    elif sats is None or sats < 88:
        print(25)  # UseSatsProbe to measure SaO2
    elif events[17] > 0.1:  # RadialPulseNonPalpable
        print(17)  # StartChestCompression
    elif sats < 88:
        print(30)  # Use Non Rebreather Mask

    # Circulation management
    elif map_value is None:
        print(27)  # UseBloodPressureCuff
    elif map_value < 60:
        print(15)  # Give Fluids

    # Check Disability and Exposure problems
    else:
        print(8)  # ExamineResponse for overall responsiveness
        print(6)  # ExamineDisability to track level of consciousness
        print(7)  # ExamineExposure to check for external causes or signs

    # Check for stabilization
    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and resp_rate >= 8)
    ):
        print(48)  # Finish - John is stabilized
        break  # Exiting the loop after finishing
    else:
        print(0)  # Default action when no immediate intervention is needed
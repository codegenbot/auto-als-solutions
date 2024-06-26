while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate life-threatening conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    # Airway Assessment
    if events[3] <= 0.1 and (events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1):
        print(3)  # ExamineAirway
        continue
    elif events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue

    # Breathing Assessment
    if (sats is not None and sats < 88) or events[8] > 0.1:  # Breathing diff. issues & Low Sats
        print(30)  # Use Non Rebreather Mask
        continue

    # Circulation Assessment
    if events[17] > 0.1:  # RadialPulseNonPalpable
        print(17)  # StartChestCompression
        continue
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Disability and Exposure
    if events[21] > 0.1:  # AVPU_U
        print(36)  # PerformHeadTiltChinLift
        continue

    # Check for stabilization
    if (sats is not None and sats >= 88) and (map_value is not None and map_value >= 60) and (resp_rate is not None and resp_rate >= 8):
        print(48)  # Finish - John is stabilized
        break

    # Default action when no specific intervention is necessary
    print(0)  # DoNothing
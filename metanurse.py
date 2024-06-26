while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    # Current measurements if they're recent
    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Check for critical conditions
    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    # Checking Airway
    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
        continue

    # Managing Airway Problems
    if any(
        events[i] > 0.1 for i in [4, 5, 6]
    ):  # AirwayVomit, AirwayBlood, AirwayTongue
        print(31)  # Use Yankeur Suction Catheter
        continue

    # Assessing Breathing
    if events[7] > 0.1 or (
        resp_rate is not None and resp_rate < 8
    ):  # BreathingNone or bad resp rate
        print(29)  # Use Bag Valve Mask
        continue

    # Circulation Problems
    if events[17] > 0.1:  # RadialPulseNonPalpable
        print(17)  # StartChestCompression
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Hypotension management
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Final check to determine if the patient is stabilized
    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and mapenssure >= 60)
        and (resp_rate is not None and resp_rate >= 8)
    ):
        print(48)  # Finish - John is stabilized
        break

    # Default minimal action if nothing specific is needed
    print(0)  # DoNothing
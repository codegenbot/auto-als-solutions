while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate response: Major life threats
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        print(17)  # Start Chest Compression
        continue

    # Stabilization checks
    if sats is not None and map_value is not None and resp_rate is not None:
        if sats >= 88 and map_value >= 60 and resp_rate >= 8:
            print(48)  # Finish
            break
        
    # Initial checks using examinations
    if not any(events[22:24]):  # Check if any AVPU Response Verbal/Non-Verbal/None
        print(8)  # Examine Response
        continue

    if events[3] <= 0.1:  # AirwayClear is not recently confirmed
        print(3)  # Examine Airway
        continue

    if events[7] > 0.1 or resp_rate is not None and resp_rate < 8:  # No breathing or low respiratory rate
        print(29)  # Use Bag Valve Mask
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    if map_value is not None and map_value < 60:
        print(5)  # Examine Circulation
        continue

    # Disability check: if any low responsiveness and no clear consciousness
    if events[22] < 0.1 or events[23] < 0.1:  # Decreasing AVPU response like Unresponsive or Pain responsive
        print(8)  # ExamineResponse
        continue

    # Check if exposure related symptoms needed
    if events[26] < 0.1 or events[27] < 0.1:
        print(7)  # ExamineExposure
        continue

    # Check for the effectiveness of intervention
    if times[5] <= 0.1 or (sats is not None and sats < 88):
        print(25)  # UseSatsProbe
        continue

    if map_value is not None and map_value < 70:
        print(15)  # GiveFluids
        continue

    # Default action: No critical action required
    print(0)  # DoNothing
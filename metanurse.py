while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    # Immediate checks for airway and breathing
    if events[3] > 0.1:
        print(3)  # ExamineAirway
    elif events[7] > 0.1:
        print(29)  # Use Bag Valve Mask for assisted breathing
    
    # Oxygenation and circulation check
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask to increase oxygen
    elif map_value is not None and map_value < 60:
        print(15)  # Give Fluids to improve circulation

    # Respiratory rate assessment
    if resp_rate is not None and resp_rate < 8:
        print(4)  # ExamineBreathing

    # Stable condition check
    elif (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_title >= 60
        and resp_rate is not None
        and resp_rate >= 8
        and events[3] > 0.1  # Airway check after possible intervention
    ):
        print(48)  # Finish - John is stabilized
        break
    else:
        print(0)  # Default action when no immediate intervention is needed
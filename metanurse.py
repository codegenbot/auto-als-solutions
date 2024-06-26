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

    if events[3] <= 0.1:  # ExamineAirway if relevance of AirwayClear is low
        print(3)
    elif resp_rate is not None and resp_rate < 8:
        print(29)  # Use Bag Valve Mask
    elif sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
    elif map_value is not None and map_value < 60:
        print(15)  # Give Fluids
    else:
        # Perform steps systematically
        if events[4] <= 0.1:  # Airway problems other than clear
            print(3)  # ExamineAirway
        elif events[7] <= 0.1:  # Breathing problems
            print(4)  # ExamineBreathing
        elif events[16] <= 0.1:  # Circulation issues, non palpable pulse
            print(5)  # ExamineCirc
        elif events[22] <= 0.1:  # Disability issues, AVPU scale
            print(6)  # Examine Disability
        elif times[6] == 0:  # if no recent respiration rate measurement
            print(25)  # Use Sats Probe
        elif times[4] == 0:  # if no recent MAP measurement
            print(26)  # Use Aline
        else:
            if (
                sats is not None
                and sats >= 88
                and map_value is not None
                and map_value >= 60
                and resp_rate is not None
                and resp_rate >= 8
            ):
                print(48)  # Finish
                break
            else:
                print(0)  # DoNothing when all other conditions are not met
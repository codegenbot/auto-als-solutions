stage = 0

while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            stage = 0
            continue

        if stage == 0:
            print(3)  # Examine Airway
            stage = 1
        elif stage == 1:
            if events[5] > 0.1 or events[6] > 0.1:  # Airway not clear
                print(31)  # Use Yankeur Suction Catheter
            else:
                print(4)  # Examine Breathing
                stage = 2
        elif stage == 2:
            if events[7] > 0.1:  # BreathingNone significant
                print(29)  # Use Bag Valve Mask
            else:
                print(5)  # Examine Circulation
                stage = 3
        elif stage == 3:
            if events[17] > 0.1:  # RadialPulseNonPalpable significant
                print(17)  # Start Chest Compression
            else:
                print(6)  # Examine Disability
                stage = 4
        elif stage == 4:
            print(7)  # Examine Exposure
            stage = 5
        elif stage == 5:
            if sats is not None and sats < 88:
                print(30)  # Use Non Rebreather Mask
            elif map_value is not None and map_value < 60:
                print(15)  # Give Fluids
            elif resp_rate is not None and resp_rate < 8:
                print(29)  # Use Bag Valve Mask
            else:
                print(48)  # Finish
                break  # Complete the management, break the loop as we output 'Finish'
        else:
            print(0)  # Do Nothing as a safe fallback

    except EOFMorepher details and correct parameters.
        break
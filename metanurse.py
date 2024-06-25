while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        timed_meas_sats = observations[40]
        timed_meas_map = observations[41]
        measured_sats = observations[52]
        measured_map = observations[51]

        airway_clear = observations[3]
        breathing_none = observations[7]
        resp_rate = observations[39]

        # Start chest compression if very critical
        if timed_meas_satts > 0 and measured_sats < 65:
            print(17)
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)
            continue

        # Examine airway
        if airway_clear < 0.5:
            if observations[4] or observations[5] or observations[6]:
                print(35)
            else:
                print(3)
            continue

        # Breathing
        if breathing_none > 0.5:
            print(29)
            continue
        elif timed_meas_sats > 0 and measured_sats < 88:
            print(30)
            continue

        # Circulation
        if timed_meas_map == 0 or measured_map < 60:
            print(20)
            print(27)
            print(16)
            continue

        # Disability
        if observations[21] or observations[23]:
            print(6)
            continue

        # Exposure
        print(7)

        if measured_sats >= 88 and measured_map >= 60 and not breathing_none:
            print(48)
            break

    except EOFError:
        break
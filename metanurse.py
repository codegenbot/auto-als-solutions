while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        response_verbal = observations[0]
        response_groan = observations[1]
        response_none = observations[2]
        airway_clear = observations[3]
        airway_obstruction = max(observations[4], observations[5], observations[6])
        heart_rhythm = observations[27:39]
        heart_rhythm_measure = observations[33]
        measured_hr = observations[39]
        measured_rr = observations[40]
        measured_cg = observations[41]
        measured_temp = observations[42]
        measured_map = observations[43]
        measured_sats = observations[44]
        measured_resps = observations[45]
        hr = observations[46]
        rr = observations[47]
        cg = observations[48]
        temp = observations[49]
        map_value = observations[50]
        sats = observations[51]
        resps = observations[52]

        # Critical instant lifesaving checks
        if measured_sats > 0 and sats < 65:
            print(17)  # StartChestCompression
            continue
        if measured_map > 0 and map_value < 20:
            print(17)  # StartChestCompression
            continue

        # Attach devices and examine essentials
        if measured_map == 0:
            print(27)  # UseBloodPressureCuff
            continue
        if measured_hr == 0:
            print(24)  # UseMonitorPads
            continue
        if measured_hr > 0 and measured_map > 0:
            print(5)  # ExamineCirculation
            continue

        # Check heart rhythm issues
        if any([v > 0 for v in heart_rhythm[5:9]]) or any(
            [v > 0 for v in heart_rhythm[1:2]]
        ):  # problematic rhythms
            print(11)  # GiveAmiodarone
            continue
        if heart_rhythm[1] > 0:  # SVT
            print(9)  # GiveAdenosine
            continue

        # Airway management
        if response_none > 0 or airway_obstruction > 0:
            if measured_sats == 0:
                print(25)  # UseSatsProbe
                continue
            print(3)  # ExamineAirway
            continue

        # Breathing management
        if measured_rr == 0:
            print(4)  # ExamineBreathing
            continue
        if measured_rr > 0 and rr < 8:
            print(29)  # UseBagValveMask
            continue

        # Circulation stabilization
        if map_value < 60:
            print(15)  # GiveFluids
            continue

        # O2 Saturation handling
        if sats < 88:
            if airway_clear > 0:
                print(30)  # UseNonRebreatherMask
            else:
                print(3)  # ExamineAirway
            continue

        # Final check before finishing
        if airway_clear > 0 and sats >= 88 and rr >= 8 and map_value >= 60:
            print(48)  # Finish
            break

    except EOFError:
        break
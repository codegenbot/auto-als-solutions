while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Timed events
        timed_meas_sats = observations[39]
        timed_meas_map = observations[40]
        timed_meas_resp_rate = observations[41]

        # Measurements
        measured_sats = observations[46]
        measured_map = observations[45]
        measured_resp_rate = observations[47]

        # Events
        airway_clear = observations[3]
        breathing_none = observations[7]

        # Critical conditions that need immediate action
        if timed_meas_sats > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Regular Checkup for each ABCDE category
        # A: Airway
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue

        # B: Breathing
        if breathing_none > 0:
            print(29)  # UseBagValveMask
            continue

        # C: Circulation
        if timed_meas_map == 0 or measured_map < 60:
            print(38)  # TakeBloodPressure
            continue

        # D: Disability/Consciousness
        print(6)  # ExamineDisability

        # E: Exposure
        print(7)  # ExamineExposure

        # Handling Insufficient Sats or MAP
        if (timed_meas_sats > 0 and measured_sats < 88) or (
            timed_meas_map > 0 and measured_map < 60
        ):
            if airway_clear > 0 and measured_resp_rate >= 8:
                print(30)  # UseNonRebreatherMask
            else:
                print(29)  # UseBagValveMask
            continue

        # All conditions good, can end the game
        print(48)  # Finish
        break

    except EOFError:
        break
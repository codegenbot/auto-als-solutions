while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Observations
        timed_meas_sats = observations[39]
        timed_meas_map = observations[40]
        timed_meas_resp = observations[41]
        measured_sats = observations[46]
        measured_map = observations[45]
        measured_resp = observations[47]

        airway_clear = observations[3]
        breathing_none = observations[7]

        # Immediate response needed if critical values are observed
        if timed_meas_sats > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Assessing and Reacting to Airway
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue

        # Handling Insufficient Sats or MAP
        if (timed_meas_sats > 0 and measured_sats < 88) or (
            timed_meas_map > 0 and measured_map < 60
        ):
            if airway_clear > 0:
                print(30)  # UseNonRebreatherMask
            else:
                print(3)  # ExamineAirway
            continue
        
        # Check respiratory rate
        if timed_meas_resp > 0 and measured_resp < 8:
            print(29)  # UseBagValveMask
            continue

        # All conditions good, can end the game
        print(48)  # Finish
        break

    except EOFError:
        break
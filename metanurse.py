while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parsing inputs
        airway_clear = observations[3]
        breathing_none = observations[7]
        breathing_rate_timed = observations[40]
        breathing_rate = observations[46]
        oxygen_sats_timed = observations[39]
        oxygen_sats = observations[45]
        map_timed = observations[41]
        map_measure = observations[47]

        # Critical instant lifesaving checks
        if oxygen_sats_timed > 0 and oxygen_sats < 65:
            print(17)  # StartChestCompression
            continue
        if map_timed > 0 and map_measure < 20:
            print(17)  # StartChestCompression
            continue

        # Airway management
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue

        # Breathing management
        if breathing_none > 0:
            print(29)  # UseBagValveMask
            continue
        if breathing_rate_timed > 0 and breathing_rate < 8:
            print(29)  # UseBagValveMask
            continue

        # Circulation stabilization
        if map_timed > 0 and map_measure < 60:
            print(15)  # GiveFluids
            continue

        # Check oxygenation and apply oxygen if needed
        if oxygen_sats_timed > 0 and oxygen_sats < 88:
            if airway_clear > 0:
                print(30)  # UseNonRebreatherMask
            else:
                print(3)  # ExamineAirway
            continue

        # If all stabilizing conditions are met
        print(48)  # Finish
        break

    except EOFError:
        break
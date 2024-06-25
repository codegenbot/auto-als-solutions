while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Observation indices
        response_verbal = observations[0]
        breathless = observations[1]
        clear_airway = observations[3]
        oxygen_sats = observations[52]
        breathing_rate = observations[51]
        map_measure = observations[50]

        # Conditions for checking cardiac arrest
        if oxygen_sats < 65 or map_measure < 20:
            print(17)  # StartChestCompression
            continue

        # Manage the airway
        if clear_airway > 0:
            print(0)  # DoNothing if airway is clear
        else:
            print(3)  # ExamineAirway
            continue

        # Manage breathing
        if breathing_rate < 8:
            print(29)  # UseBagValveMask
            continue
        elif 88 > oxygen_sats >= 65:
            print(30)  # UseNonRebreatherMask
            continue

        # Check circulation
        if map_measure < 60:
            print(15)  # GiveFluids
            continue

        # Assuming patient stabilized if we reach here
        print(48)  # Finish
        break

    except EOFError:
        break
while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Extracting observations
        # Event occurrences
        airway_clear = observations[3]
        airway_vomit = observations[4]
        airway_blood = observations[5]
        airway_tongue = observations[6]
        breathing_none = observations[7]
        breathing_snoring = observations[8]
        breathing_see_saw = observations[9]
        
        # Measurement times and values
        resp_rate_time = observations[40]
        resp_rate = observations[46]
        sats_time = observations[39]
        sats = observations[45]
        map_time = observations[41]
        map_value = observations[47]
        
        # Heart rhythms
        heart_rhythm_svt = observations[29]
        heart_rhythm_af = observations[30]
        heart_rhythm_vt = observations[32]

        # Critical life-threatening conditions
        if (sats_time > 0 and sats < 65) or (map_time > 0 and map_value < 20):
            print(17)  # StartChestCompression
            continue

        # Airway management
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue
        elif airway_blood > 0 or airway_vomit > 0 or airway_tongue > 0:
            print(31)  # UseYankeurSuctionCatheter
            continue

        # Breathing management
        if breathing_none > 0:
            print(29)  # UseBagValveMask
            continue
        elif breathing_snoring > 0 or breathing_see_saw > 0:
            print(29)  # UseBagValveMask
            continue
        if resp_rate_time > 0 and resp_rate < 8:
            print(29)  # UseBagValveMask
            continue

        # Oxygen management
        if sats_time > 0 and sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Circulation management
        if map_time > 0 and map_value < 60:
            print(15)  # GiveFluids
            continue

        # Heart rhythm management
        if heart_rhythm_svt > 0:
            print(9)  # GiveAdenosine
            continue
        elif heart_rhythm_af > 0 or heart_rhythm_vt > 0:
            print(28)  # AttachDefibPads
            continue

        # If all conditions are stabilized
        print(48)  # Finish
        break

    except EOFError:
        break
while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        airway_clear = observations[3]
        airway_vomit = observations[4]
        airway_blood = observations[5]
        breathing_none = observations[7]
        breathing_rate_timed = observations[40]
        breathing_rate = observations[46]
        oxygen_sats_timed = observations[39]
        oxygen_sats = observations[45]
        map_timed = observations[41]
        map_measure = observations[47]
        heart_rhythm_svt = observations[29]
        heart_rhythm_af = observations[30]
        heart_rhythm_vt = observations[32]

        # Step 1: Check if immediate life-saving measures are required
        if (oxygen_sats_timed > 0 and oxygen_sats < 65) or (map_timed > 0 and map_measure < 20):
            print(17)  # StartChestCompression
            continue

        # Step 2: Update latest patient status
        print(3)  # ExamineAirway
        print(4)  # ExamineBreathing
        print(5)  # ExamineCirculation
        print(25) # UseSatsProbe
        print(28) # AttachDefibPads

        # Step 3: Manage airway
        if airway_clear == 0:
            print(3)  # ExamineAirway
        elif airway_blood > 0 or airway_vomit > 0:
            print(31)  # UseYankeurSuctionCatheter

        # Step 4: Manage breathing
        if breathing_none > 0:
            print(29)  # UseBagValveMask

        # Step 5: Manage oxygenation
        if oxygen_sats_timed > 0 and oxygen_sats < 88:
            print(30)  # UseNonRebreatherMask

        # Step 6: Manage circulation
        if map_timed > 0 and map_measure < 60:
            print(15)  # GiveFluids

        # Step 7: Check and manage heart rhythm
        if heart_rhythm_svt > 0:
            print(9)  # GiveAdenosine
        elif heart_rhythm_af > 0 or heart_rhythm_vt > 0:
            print(10)  # GiveAdrenaline

        # Step 8: Finish if stabilized
        if airway_clear > 0 and oxygen_sats >= 88 and (breathing_rate_timed > 0 and breathing_rate >= 8) and (map_timed > 0 and map_measure >= 60):
            print(48)  # Finish
            break

    except EOFError:
        break
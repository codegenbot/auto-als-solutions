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

        # Life-threatening immediate actions
        if (oxygen_sats_timed > 0 and oxygen_sats < 65) or (
            map_timed > 0 and map_measure < 20
        ):
            print(17)  # StartChestCompression
            continue

        # Initial examination
        if airway_clear == 0 and airway_vomit == 0 and airway_blood == 0:
            print(3)  # ExamineAirway
            continue

        # Airway management
        if airway_blood > 0 or airway_vomit > 0:
            print(31)  # UseYankeurSuctionCatheter
            continue

        # Breathing management
        if breathing_none > 0:
            print(29)  # UseBagValveMask
            continue
        elif (breathing_rate_timed > 0 and breathing_rate < 8) or (
            oxygen_sats_timed > 0 and oxygen_sats < 88
        ):
            print(30)  # UseNonRebreatherMask
            continue

        # Circulation management
        if map_timed == 0 or map_measure < 60:
            print(38)  # TakeBloodPressure
            continue
        if map_measure < 60:
            print(15)  # GiveFluids
            continue

        # Heart rhythm management
        if heart_rhythm_svt > 0:
            print(9)  # GiveAdenosine
            continue
        elif heart_rhythm_af > 0 or heart_rhythm_vt > 0:
            print(28)  # AttachDefibPads
            continue

        if (
            oxygen_sats_timed == 0
            or oxygen_sats > 88
            and breathing_rate_timed == 0
            or breathing_rate >= 8
            and map_timed == 0
            or map_measure >= 60
        ):
            print(48)  # Finish
            break

    except EOFEasyError:
        break
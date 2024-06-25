while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parsing inputs
        airway_clear = observations[3]
        airway_vomit = observations[4]
        airway_blood = observations[5]

        breathing_none = observations[7]
        breathing_rate_timed = observations[40]
        breathing_rate = observations[46]

        sats_timed = observations[39]
        sats = observations[45]

        map_timed = observations[41]
        map_measure = observations[47]

        heart_rhythm_svt = observations[29]
        heart_rhythm_af = observations[30]
        heart_rhythm_vt = observations[32]

        # Critical conditions leading to immediate CPR
        if (sats_timed > 0 and sats < 65) or (map_timed > 0 and map_measure < 20):
            print(17)  # StartChestCompression
            continue

        # Airway management
        if airway_clear == 0 or airway_blood > 0 or airway_vomit > 0:
            print(3)  # ExamineAirway
            continue
        if airway_blood > 0 or airway_vomit > 0:
            print(31)  # UseYankeurSuctionCatheter
            continue

        # Breathing management
        if breathing_none > 0:
            print(29)  # UseBagValveMask
            continue
        elif breathing_rate_timed > 0 and breathing_rate < 8:
            print(29)  # UseBagValveMask
            continue

        # Oxygen saturation management
        if sats_timed > 0 and sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Circulation stabilization
        if map_timed > 0 and map_measure < 60:
            print(15)  # GiveFluids
            continue

        # Heart rhythm disturbances
        if heart_rhythm_vt > 0:
            print(28)  # AttachDefibPads
            continue
        if heart_rhythm_svt > 0:
            print(9)  # GiveAdenosine
            continue
        if heart_rhythm_af > 0:
            print(28)  # AttachDefibPads
            continue

        # If all is stable, finish
        print(48)  # Finish
        break

    except EOFError:
        break
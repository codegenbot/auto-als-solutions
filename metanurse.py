while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parsing inputs
        airway_clear = observations[3]
        airway_vomit = observations[4]
        airway_blood = observations[5]

        # Airway Checks
        if airway_clear == 0 or airway_vomit > 0 or airway_blood > 0:
            print(3)  # ExamineAirway
            continue

        breathing_none = observations[7]
        breathing_rate = observations[46]

        sats = observations[45]

        map_measure = observations[47]

        heart_rhythm_af = observations[30]
        heart_rhythm_vt = observations[32]

        # Critical conditions leading to immediate actions
        if sats < 65 or map_measure < 20:
            if sats < 65:
                print(17)  # StartChestCompression
            elif map_measure < 20:
                print(17)  # StartChestCompression
            continue

        # Airway management
        if airway_vomit > 0 or airway_blood > 0:
            print(31)  # UseYankeurSuctionCatheter
            print(3)  # Re-examineAirway
            continue

        # Breathing management
        if breathing_none > 0 or breathing_rate < 8:
            print(29)  # UseBagValveMask
            continue

        # Oxygen saturation management
        if sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Circulation stabilization
        if map_measure < 60:
            print(15)  # GiveFluids
            continue

        # Heart rhythm disturbances
        if heart_rhythm_vt > 0:
            print(28)  # AttachDefibPads
            continue
        if heart_rhythm_af > 0:
            print(28)  # AttachDefibPads
            continue

        # Final condition check before finishing
        if airway_clear > 0 and sats >= 88 and breathing_rate >= 8 and map_measure >= 60:
            print(48)  # Finish
        else:
            print(16)  # Final status check Fail Safe
        break

    except EOFError:
        break
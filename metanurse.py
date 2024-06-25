while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        airway_clear = observations[3]
        breathing_none = observations[7]
        measured_sats = observations[46] if observations[39] > 0 else None
        measured_map = observations[45] if observations[40] > 0 else None

        if breathing_none > 0:
            # Immediate intervention as John has stopped breathing
            print(29)  # UseBagValveMask
        elif measured_sats is not None and measured_map is not None:
            if measured_sats < 65 or measured_map < 20:
                print(17)  # StartChestCompression
            elif measured_sats < 88 or measured_map < 60:
                if airway_clear > 0:
                    print(30)  # UseNonRebreatherMask
                else:
                    print(3)  # ExamineAirway
            else:
                print(48)  # Finish
        else:
            if airway_clear > 0:
                print(4)  # ExamineBreathing
            else:
                print(3)  # ExamineAirway
    except EOFError:
        break
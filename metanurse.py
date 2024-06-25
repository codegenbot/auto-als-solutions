while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Assuming correct indices for measured sats and map according to problem statement clarification
        measured_sats = observations[53]
        measured_map = observations[52]

        # Implementing ABCDE strategy
        if measured_sats < 65 or measured_map < 20:
            # Check if `StartChestCompression` is valid here—if still not, find an alternative
            print(17)  # StartChestCompression
        elif (
            observations[39 + 6] * measured_sats < 88
            or observations[39 + 5] * measured_map < 60
        ):
            airway_state = observations[3:7]  # AirwayClear to AirwayTongue
            if all(
                i == 0 for i in airway_state
            ):  # All airway checks are zero, need to examine
                print(3)  # ExamineAirway
            elif measured_sats < 88:
                # Check breathing and provide appropriate oxygen support
                print(30)  # UseNonRebreatherMask
            elif measured_map < 60:
                # Check circulation more deeply
                print(5)  # ExamineCirculation
        else:
            print(48)  # Finish
    except EOFError:
        break
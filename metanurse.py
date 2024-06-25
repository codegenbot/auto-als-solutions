while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))
        measured_sats = observations[53 - 1]  # Last item
        measured_map = observations[52 - 1]  # Second to last item

        # Check conditions to perform actions
        if measured_sats < 65 or measured_map < 20:
            print(17)  # StartChestCompression
        elif measured_sats < 88 or measured_map < 60:
            airway_clear = observations[3] > 0  # AirwayClear index
            if airway_clear:
                print(30)  # UseNonRebreatherMask
            else:
                print(3)  # ExamineAirway
        else:
            print(48)  # Finish - Stabilized
    except EOFError:
        break
while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))
        measured_sats = observations[53 - 1]  # Last item
        measured_map = observations[52 - 1]  # Second to last item

        # Perform ABCDE assessment and act accordingly
        airway_clear = observations[3]  # AirwayClear index
        breathing_problems = (
            observations[7] > 0 or observations[8] > 0
        )  # BreathingNone, BreathingSnoring

        if measured_sats < 65 or measured_map < 20:
            print(17)  # StartChestCompression
        elif measured_sats < 88 or measured_map < 60:
            if airway_clear > 0:
                if measured_sats < 88:
                    print(30)  # UseNonRebreatherMask
                else:
                    print(15)  # GiveFluids if MAP is low
            else:
                print(3)  # ExamineAirway
        elif airway_clear == 0 or breathing_problems:
            print(3)  # ExamineAirway
        elif measured_sats >= 88 and measured_map >= 60:
            print(48)  # Finish - Stabilized
        else:
            print(0)  # DoNothing, continue to monitor
    except EOFRelicsError:
        break
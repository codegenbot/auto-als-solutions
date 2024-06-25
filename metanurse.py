while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))
        measured_sats = observations[53 - 1]  # Last item
        measured_map = observations[52 - 1]  # Second to last item
        airway_clear = observations[3] > 0  # AirwayClear index
        breathing_none = observations[7] > 0  # BreathingNone index

        # Check critical conditions first
        if measured_sats < 65 or measured_map < 20:
            print(17)  # StartChestCompression
        
        # Check if stabilization is needed
        elif measured_sats < 88 or measured_map < 60:
            if not airway_clear:
                print(3)  # ExamineAirway
            elif breathing_none:
                print(29)  # UseBagValveMask
            else:
                print(5)  # ExamineCirculation

        # If stabilized, finish the simulation
        else:
            print(48)  # Finish

    except EOFError:
        break
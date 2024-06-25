while True:
    try:
        observations = list(map(float, input().strip().split()))
        relevance_sats = observations[40]
        relevance_map = observations[41]
        measured_sats = observations[46]
        measured_map = observations[47]

        # Switch state based on conditions
        if state == 'airway':
            if observations[3] > 0:  # AirwayClear
                state = 'breathing'
            else:
                print(3)  # ExamineAirway

        elif state == 'breathing':
            if observations[7] > 0:  # BreathingNone
                print(29)  # UseBagValveMask
            else:
                state = 'circulation'

        elif state == 'circulation':
            # Check measures and relevant actions for circulation
            if measured_sats is None or measured_map is None:
                print(16)  # ViewMonitor
            elif measured_sats < 88 or measured_map < 60:
                print(15)  # GiveFluids
            else:
                state = 'complete'

        elif state == 'complete':
            print(48)  # Finish
            break

        # Check critical thresholds
        if (measured_sats is not None and measured_sats < 65) or (measured_map is not None and measured_map < 20):
            print(17)  # StartChestCompression
            break

    except EOFError:
        break
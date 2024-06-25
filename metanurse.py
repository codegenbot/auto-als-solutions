state = 'airway'  # Starting with airway check per ABCDE

while True:
    try:
        observations = list(map(float, input().strip().split()))
        relevance_sats = observations[40]
        relevance_map = observations[41]
        measured_sats = observations[46]
        measured_map = observations[47]

        if relevance_sats == 0:
            measured_sats = None
        if relevance_map == 0:
            measured_map = None

        if state == 'airway':
            if observations[3] > 0:  # AirwayClear
                state = 'breathing'
                print(4)  # ExamineBreathing
            else:
                print(3)  # ExamineAirway

        elif state == 'breathing':
            if observations[10] > 0 or observations[11] > 0 or observations[12] > 0:  # Problematic breathing signs
                print(29)  # UseBagValveMask
                state = 'circulation'  # Assume issue handled, proceed
            else:
                state = 'circulation'
                print(25)  # UseSatsProbe to get more info

        elif state == 'circulation':
            if measured_sats is None or measured_map is None:
                print(27)  # UseBloodPressureCuff
                print(16)  # ViewMonitor
            else:
                if measured_sats < 65 or measured_map < 20:
                    print(17)  # StartChestCompression
                elif measured_sats < 88 or measured_map < 60:
                    print(15)  # GiveFluids
                else:
                    state = 'complete'

        elif state == 'complete':
            print(48)  # Finish
            break

    except EOFError:
        break
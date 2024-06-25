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
            elif observations[4] > 0:  # AirwayVomit
                print(31)  # UseYankeurSuctionCatheter
            elif observations[5] > 0:  # AirwayBlood
                print(31)  # UseYankeurSuctionCatheter
            elif observations[6] > 0:  # AirwayTongue
                print(32)  # UseGuedelAirway
            else:
                print(3)  # ExamineAirway

        elif state == 'breathing':
            if observations[7] > 0:  # BreathingNone
                print(29)  # UseBagValveMask
            elif measured_sats is not None and measured_sats < 88:
                print(30)  # UseNonRebreatherMask
            else:
                state = 'circulation'
                print(5)  # ExamineCirculation

        elif state == 'circulation':
            if measured_sats is not None and measured_map is not None:
                if measured_sats < 65 or measured_map < 20:
                    print(17)  # StartChestCompression
                elif measured_sats < 88 or measured_map < 60:
                    print(15)  # GiveFluids
                else:
                    state = 'complete'
            elif observations[16] == 0:  # RadialPulseNonPalpable
                print(17)  # StartChestCompression
            else:
                print(16)  # ViewMonitor

        elif state == 'complete':
            print(48)  # Finish
            break

    except EOFStrError:
        break
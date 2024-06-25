state = "airway"

while True:
    try:
        observations = list(map(float, input().strip().split()))
        relevance_sats = observations[48]
        relevance_map = observations[48]
        measured_sats = observations[53]
        measured_map = observations[53]

        if relevance_sats == 0:
            measured_sats = None
        if relevance_map == 0:
            measured_map = None

        if state == "airway":
            if observations[3] > 0:  # AirwayClear
                state = "breathing"
                print(4)  # ExamineBreathing
            elif (
                observations[4] > 0 or observations[5] > 0 or observations[6] > 0
            ):  # AirwayVomit, AirwayBlood, AirwayTongue
                print(31)  # UseYankeurSucionCatheter
            else:
                print(3)  # ExamineAirway

        elif state == "breathing":
            if observations[7] > 0:  # BreathingNone
                if observations[6] > 0:  # AirwayTongue
                    print(37)  # PerformJawThrust
                else:
                    print(29)  # UseBagValveMask
            elif (
                observations[8] > 0 or observations[9] > 0
            ):  # BreathingSnoring, BreathingSeeSaw
                if observations[3] > 0:  # AirwayClear
                    print(30)  # UseNonRebreatherMask
                else:
                    print(36)  # PerformHeadTiltChinLift
            else:
                state = "circulation"
                print(5)  # ExamineCirculation

        elif state == "circulation":
            if (measured_sats is not None and measured_sats < 65) or (
                measured_map is not None and measured_map < 20
            ):
                print(17)  # StartChestCompression
            elif (measured_sats is not None and measured_sats < 88) or (
                measured_map is not None and measured_map < 60
            ):
                print(15)  # GiveFluids
            else:
                state = "complete"
                print(16)  # ViewMonitor

        elif state == "complete":
            if (
                (measured_sats is not None and measured_sats >= 88)
                and (measured_map is not None and measured_map >= 60)
                and observations[3] > 0
            ):  # AirwayClear
                print(48)  # Finish
                break
            else:
                state = "airway"
                print(3)  # ExamineAirway

    except EOFError:
        break
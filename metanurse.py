while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        relevance_sats = observations[40]
        relevance_resp = observations[41]
        relevance_map = observations[42]

        airway_clear = observations[3]
        measured_sats = observations[46]
        measured_resp = observations[47]
        measured_map = observations[48]

        response_verbal = observations[0]

        # Handle end of simulation case
        if measured_sats >= 88 and measured_resp >= 8 and measured_map >= 60:
            print(48)  # Finish
            continue

        if relevance_sats == 0 or relevance_resp == 0 or relevance_map == 0:
            print(25)  # UseSatsProbe to get sats
            continue

        # Immediate life-threatening checks
        if measured_sats < 65 or measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # A - Airway check
        if airway_clear <= 0.0:
            print(3)  # ExamineAirway
            continue

        # B - Breathing checks
        if measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # C - Circulation checks
        if measured_map < 60:
            print(15)  # GiveFluids
            continue

        # Finding weakest link or rechecking
        if airway_clear > 0 and measured_sats >= 88 and measured_map >= 60:
            print(4)  # ExamineBreathing handle advance life supports
        elif response_verbal == 0:
            print(8)  # ExamineResponse
        else:
            print(16)  # ViewMonitor as fallback to ensure all observations are relevant

    except EOFError:
        break
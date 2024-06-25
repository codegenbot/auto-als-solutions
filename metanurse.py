while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parsing inputs
        events = observations[:39]
        measurements_timed = observations[39:46]
        measurements = observations[46:53]

        # Event indexes
        AIRWAY_CLEAR_IDX = 3
        BREATHING_NONE_IDX = 7
        MEASURED_MAP_IDX = 41
        MEASURED_SATS_IDX = 39
        MEASURED_RESP_RATE_IDX = 40

        # Measurement indexes
        MAP_VAL_IDX = 5
        SATS_VAL_IDX = 4
        RESP_RATE_VAL_IDX = 1

        # Assigning events and measured variables
        airway_clear = events[AIRWAY_CLEAR,# 
        breathing_none = events[BREATHING_NONE_IDX]
        measured_map_timed = measurements_timed[MEASURED_MAP_IDX - 39]
        measured_sats_timed = measurements_timed[MEASURED_SATS_IDX - 39]
        measured_resp_rate_timed = measurements_timed[MEASURED_RESP_RATE_IDX - 39]

        map_val = measurements[MAP_VAL_IDX]
        sats_val = measurements[SATS_VAL_IDX]
        resp_rate_val = measurements[RESP_RATE_VAL_IDX]

        # Critical conditions check
        if measured_sats_timed > 0 and sats_val < 65:
            print(17)  # StartChestCompression
            continue
        if measured_map_timed > 0 and map_val < 20:
            print(17)  # StartChestCompression
            continue

        # Check necessary basic exams first if details are outdated
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue
        if measured_resp_rate_timed <= 0:
            print(4)  # ExamineBreathing
            continue
        if measured_map_timed <= 0:
            print(5)  # ExamineCirculation
            continue
        if measured_sats_timed <= 0:
            print(25)  # UseSatsProbe
            continue

        # Airway management
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue

        # Breathing management
        if breathing_none > 0 or (measured_resp_rate_timed > 0 and resp_rate_val < 8):
            print(29)  # UseBagValveMask
            continue

        # Circulation management
        if measured_map_timed > 0 and map_val < 60:
            print(15)  # GiveFluids
            continue

        # Oxygenation management
        if measured_sats_timed > 0 and sats_val < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # If all required conditions are stabilized
        if (measured_sats_timed > 0 and sats_val >= 88) and \
           (measured_resp_rate_timed > 0 and resp_rate_val >= 8) and \
           (measured_map_timed > 0 and map_val >= 60):
            print(48)  # Finish
            break

    except EOFError:
        break
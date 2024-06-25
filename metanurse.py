while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parsing inputs
        # Event relevance
        response_verbal = observations[1]
        response_groan = observations[2]
        response_none = observations[3]
        airway_clear = observations[4]
        airway_obstructed = observations[5] + observations[6] + observations[7]
        
        # Vital signs observations
        measured_hr_time = observations[39]
        measured_hr = observations[46]
        measured_rr_time = observations[40]
        measured_rr = observations[47]
        measured_map_time = observations[41]
        measured_map = observations[48]
        measured_sats_time = observations[42]
        measured_sats = observations[49]

        # Critical conditions check
        if measured_sats_time > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if measured_map_time > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Airway management
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue
        
        # Clearing Airway Obstructions
        if airway_obstructed > 0:
            print(31)  # UseYankeurSucionCatheter
            continue

        # Breathing management
        if measured_rr_time > 0 and measured_rr < 8:
            print(29)  # UseBagValveMask
            continue
        
        # Circulation management
        if measured_map_time > 0 and measured_map < 60:
            print(15)  # GiveFluids
            continue

        # Oxygen management
        if measured_sats_time > 0 and measured_sats < 88:
            if airway_clear > 0:
                print(30)  # UseNonRebreatherMask
            else:
                print(36)  # PerformHeadTiltChinLift
            continue
        
        # Checking vital signs are stabilized
        if measured_sats_time > 0 and measured_sats >= 88 and measured_rr_time > 0 and measured_rr >= 8 and measured_map_time > 0 and measured_map >= 60:
            print(48)  # Finish
            break

    except EOFError:
        break
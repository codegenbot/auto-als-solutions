while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parsing inputs
        events = observations[:39]
        recent_measurements = observations[39:46]
        measurements = observations[46:]

        airway_clear = events[3]
        airway_vomit = events[4]
        airway_blood = events[5]
        breathing_none = events[7]
        measured_resp_rate = recent_measurements[1]
        resp_rate = measurements[1]
        measured_sats = recent_measurements[5]
        sats = measurements[5]
        measured_map = recent_measurements[4]
        map_measure = measurements[4]
        heart_rhythm_svt = events[29]
        heart_rhythm_af = events[30]
        heart_rhythm_vt = events[32]

        # Critical checks
        if (measured_sats > 0 and sats < 65) or (measured_map > 0 and map_measure < 20):
            print(17)  # StartChestCompression
            continue

        # Airway management
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue
        elif airway_blood > 0 or airway_vomit > 0:
            print(31)  # UseYankeurSuctionCatheter
            continue

        # Breathing management
        if breathing_none > 0:
            print(29)  # UseBagValveMask
            continue
        elif measured_resp_rate > 0 and resp_rate < 8:
            print(29)  # UseBagValveMask
            continue

        # Oxygenation
        if measured_sats > 0 and sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Circulation stabilization
        if measured_map > 0 and map_measure < 60:
            print(15)  # GiveFluids
            continue
        
        # Heart rhythm management
        if heart_rhythm_svt > 0:
            print(9)  # GiveAdenosine
            continue
        elif heart_rhythm_af > 0 or heart_rhythm_vt > 0:
            print(28)  # AttachDefibPads
            continue

        # If all stabilizing conditions are met
        print(48)  # Finish
        break

    except EOFError:
        break
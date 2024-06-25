while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Observations with their indices based on problem statement
        timed_meas_sats = observations[39]
        timed_meas_map = observations[40]
        timed_meas_resp = observations[41]
        measured_sats = observations[46]
        measured_map = observations[45]
        measured_resp = observations[47]

        # Events related to airway state
        airway_clear = observations[3]
        airway_vomit = observations[4]
        airway_blood = observations[5]
        airway_tongue = observations[6]

        # Breathing observations
        breathing_none = observations[7]

        # Immediate critical situation requiring CPR
        if timed_meas_sats > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Assessing Airway
        if airway_clear == 0:
            if airway_vomit > 0 or airway_blood > 0 or airway_tongue > 0:
                print(31)  # UseYankeurSucionCatheter
                continue
            else:
                print(3)  # ExamineAirway
                continue
        else:
            # Airway is clear, proceed to check breathing
            if breathing_none > 0:
                print(29)  # UseBagValveMask
                continue

        # Evaluating breathing conditions
        if timed_meas_resp > 0 and measured_resp < 8:
            print(29)  # UseBagValveMask
            continue

        # Evaluating Oxygen Saturation and MAP for potential treatments
        if timed_meas_sats > 0 and measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if timed_meas_map > 0 and measured_map < 60:
            print(15)  # GiveFluids
            continue

        # Checking and stabilizing Circulation
        print(5)  # ExamineCirculation
        continue

    except EOFError:
        break
while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Observations
        timed_meas_sats = observations[39]
        timed_meas_map = observations[40]
        timed_meas_resp = observations[41]
        measured_sats = observations[46]
        measured_map = observations[45]
        measured_resp = observations[47]

        airway_clear = observations[3]
        breathing_none = observations[7]
        
        # Immediate critical conditions check
        if timed_meas_sats > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Examine vital signs more dynamically and accurately
        if timed_meas_sats == 0 or measured_sats < 88:
            print(25)  # UseSatsProbe
            continue
        if timed_meas_map == 0 or measured_map < 60:
            print(27)  # UseBloodPressureCuff
            continue

        # Handle Airway issues
        if airway_clear < 0.5:  # Assuming some threshold for airway clear being meaningful
            print(3)  # ExamineAirway
            continue

        # Breathing and ventilation checks
        if timed_meas_resp == 0 or measured_resp < 8:
            print(29)  # UseBagValveMask
            continue

        # Ensure all critical conditions are stable before finishing
        if measured_sats >= 88 and measured_map >= 60 and measured_resp >= 8:
            print(48)  # Finish
            break
        else:
            if measured_sats < 88:
                print(30)  # UseNonRebreatherMask
            elif measured_map < 60:
                print(15)  # GiveFluids
            elif measured_resp < 8:
                print(29)  # UseBagValveMask
            continue

    except EOFError:
        break
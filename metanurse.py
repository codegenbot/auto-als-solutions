while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Observations
        timed_meas_sats = observations[40]
        timed_meas_map = observations[41]
        measured_sats = observations[52]
        measured_map = observations[51]

        airway_clear = observations[3]
        breathing_none = observations[7]
        resp_rate = observations[46]  # Measured respiratory rate

        # Initial checks for critical conditions
        if timed_meas_sats > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Examine Airway
        if airway_clear < 0.5:
            if observations[4] > 0.5 or observations[5] > 0.5 or observations[6] > 0.5:  # Check for Vomit, Blood, Tongue obstruction
                print(35)  # PerformAirwayManoeuvres            
            else:
                print(3)  # ExamineAirway
            continue

        # Breathing Management
        if breathing_none > 0.5 or (timed_meas_sats > 0 and measured_sats < 88):
            print(29)  # UseBagValveMask
            continue

        # Address Insufficient Oxygen Saturation
        if timed_meas_sats > 0 and measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Circulation Checks
        if timed_meas_map == 0 or measured_map < 60:
            print(20)  # OpenCirculationDrawer
            print(27)  # UseBloodPressureCuff
            print(16)  # GiveFluids
            continue

        # Disability Examination
        if observations[22] or observations[23]:  # Check for unresponsive or pain response
            print(6)  # ExamineDisability
            continue

        # Exposure Check
        print(7)  # ExamineExposure
        continue

        # End game if stabilized
        if measured_sats >= 88 and measured_map >= 60 and resp_rate >= 8:
            print(48)  # Finish
            break

    except EOFError:
        break
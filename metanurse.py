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
        resp_rate = observations[39]  # Measured respiratory rate
        heart_rate = observations[38]  # Measured heart rate

        # Immediate critical checks
        if timed_meas_sats > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            print(28)  # AttachDefibPads
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Measurements setup
        if timed_meas_sats == 0:
            print(25)  # UseSatsProbe
            continue
        if timed_meas_map == 0:
            print(27)  # UseBloodPressureCuff
            continue
        if not heart_rate:
            print(16)  # ViewMonitor
            continue

        # Check Airway
        if airway_clear == 0 or airway_clear < 0.5:
            if breathing_none > 0.5:
                print(32)  # UseGuedelAirway
            else:
                print(3)  # ExamineAirway
            continue

        # Check Breathing
        if timed_meas_sats > 0 and (measured_sats < 88 or breathing_none > 0.5):
            if breathing_none > 0.5:
                print(29)  # UseBagValveMask
            else:
                print(4)  # ExamineBreathing
            continue

        # Check Circulation
        if timed_meas_map == 0 or measured_map < 60 or resp_rate < 8:
            if resp_rate < 8:
                print(29)  # UseBagValveMask
            else:
                print(5)  # ExamineCirculation
            continue

        # Sufficient oxygen saturation stabilization
        if measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # If all vital conditions are stable
        if measured_sats >= 88 and measured_map >= 60 and resp_rate >= 8:
            print(48)  # Finish
            break

    except EOFError:
        break
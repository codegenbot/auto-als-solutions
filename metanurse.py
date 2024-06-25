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
        
        # Initial checks for critical conditions
        if timed_meas_sats > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue
        
        # Examine Airway
        if airway_clear == 0 or airway_clear < 0.5:
            print(3)  # ExamineAirway
            continue
        
        # Check Breathing
        if timed_meas_sats > 0 and (measured_sats < 88 or breathing_none > 0.5):
            print(4)  # ExamineBreathing
            continue
        
        # Address Insufficient Oxygen Saturation
        if timed_meas_sats > 0 and measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue
        
        # Check Circulation
        if timed_meas_map == 0 or measured_map < 60:
            print(5)  # ExamineCirculation
            continue
        
        # Assistance for Breathing if needed
        if resp_rate < 8 and resp_rate > 0:
            print(29)  # UseBagValveMask
            continue
        
        # If all conditions are stable
        if measured_sats >= 88 and measured_map >= 60:
            print(48)  # Finish
            break
        
    except EOFError:
        break
while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Parse inputs
        measured_recency = observations[33:40]
        measurements = observations[40:47]
        airway_clear = observations[3]
        airway_vomit = observations[4]
        airway_blood = observations[5]
        breathing_none = observations[7]
        
        heart_rate_recency = measured_recency[0]
        respir_rate_recency = measured_recency[1]
        glucose_recency = measured_recency[2]
        temperature_recency = measured_recency[3]
        map_recency = measured_recency[4]
        sats_recency = measured_recency[5]
        resps_recency = measured_recency[6]
        
        heart_rate = measurements[0]
        respir_rate = measurements[1]
        glucose = measurements[2]
        temperature = measurements[3]
        map_measure = measurements[4]
        sats = measurements[5]
        resps = measurements[6]
        
        # Immediate critical conditions
        if (sats_recency > 0 and sats < 65) or (map_recency > 0 and map_measure < 20):
            print(17)  # StartChestCompression
            continue
        
        # Examine airway if not clear or when status unknown
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue
        elif airway_blood > 0 or airway_vomit > 0:
            print(31)  # UseYankeurSuctionCatheter
            continue
        
        # Breathing checks
        if breathing_none > 0:
            print(29)  # UseBagValveMask
            continue
        if respir_rate_recency == 0 or resps < 8:
            print(4)  # ExamineBreathing
            continue
        
        # Sufficient oxygenation assessment
        if sats_recency == 0 or sats < 88:
            print(25)  # UseSatsProbe
            continue
        
        # Circulation checks
        if map_recency == 0 or map_measure < 60:
            print(27)  # UseBloodPressureCuff
            continue
        if (map_recency > 0 and map_measure >= 60 and sats_recency > 0 and sats >= 88 and respir_rate_recency > 0 and resps >= 8):
            print(48)  # Finish
            break
        
        # Default fall-back action
        print(0)  # DoNothing

    except EOFError:
        break
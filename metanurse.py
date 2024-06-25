while True:
    inputs = input().strip().split()
    if not inputs:
        break

    events = [float(e) for e in inputs[:39]]
    recencies = [float(t) for t in inputs[39:46]]
    measurements = [float(m) for m in inputs[46:]]

    # Utilize latest measurements where recent data exists
    sats = measurements[5] if recencies[5] > 0 else None
    map_value = measurements[4] if recencies[4] > 0 else None
    resp_rate = measurements[6] if recencies[6] > 0 else None

    # Critical conditions lead to immediate resuscitation measures
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        print(17)  # Critical condition, start chest compression
        continue
    
    # Evaluate airway based on airway related events, condition persistence
    if events[7] > 0.1:  # Significant lack of breathing
        print(29)  # Use Bag Valve Mask
        continue
    
    # Lower than adequate oxygen levels, breathing assistance
    if sats is not None and sats < 88:
        print(30)  # Use Non-Rebreather Mask
        continue

    # Circulatory intervention if BP is low
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # All conditions met for patient stabilization, exit condition
    if (sats is not None and sats >= 88) and (map_value is not None and map_value >= 60) and (resp_rate is not None and resp_rate >= 8):
        print(48)  # Safely Finish the scenario
        break

    # No action identified, continue monitoring
    print(0)
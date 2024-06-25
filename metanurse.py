while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    heart_rate = measurements[0] if times[0] > 0 else None

    # Immediate critical conditions
    if sats is not None and sats < 65 or map_value is not None and map_value < 20:
        print(17)  # Start Chest Compression
        continue

    # ABC Checks
    if events[3] < 0.1 and (events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1):
        print(3)  # Examine Airway
    elif events[7] > 0.1 or events[8] > 0.1 or events[9] > 0.1:  # Breathing issues
        print(4)  # Examine Breathing
    elif events[16] < 0.7:  # No palpable pulse
        print(5)  # Examine Circulation
    else:
        # Conditions based on measurements and observations
        if sats is not None and sats < 88:
            print(30)  # Use Non Rebreather Mask
        elif map_value is not None and map_value < 60:
            print(15)  # Give Fluids
        elif heart_rate is not None and heart_respsate < 30:
            print(10)  # Give Adrenaline
        elif resp_rate is not None and resp_rate < 8:
            print(29)  # Use Bag Valve Mask
        else:
            # Check rhythm if unstable vitals
            if heart_rate is not None and (heart_rate < 60 or heart_rate > 100):
                print(2)  # Check Rhythm
            else:
                # Re-check all vitals if everything seems fine up until now
                if sats is not None and sats >= 88 and map_value is not None and map_value >= 60 and resp_rate is not None and resp_rate >= 8:
                    print(48)  # Finish Scenario
                    break
                else:
                    # If unsure, perform general examinations
                    print(8)  # Examine Response (General Check)
                    continue

    # Do Nothing if no actions matched
    print(0)  # DoNothing, continue monitoring
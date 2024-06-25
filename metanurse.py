while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate Response to Critical Conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_data < 20):
        print(17)  # Start Chest Compression
        continue

    # Airway Management
    if events[3] < 0.1:  # Airway not recently checked
        print(3)  # Examine Airway
        continue
    if events[4] > 0.1 or events[5] > 0.1:  # Presence of Vomit or Blood
        print(31)  # Use Yankeur Suction Catheter
        continue

    # Breathing Assessment
    if events[7] > 0.1:  # Breathing None
        print(29)  # Use Bag Valve Mask
        continue

    # Circulation Check
    if events[28] > 0.1 or events[29] > 0.1 or events[30] > 0.1:  # Dangerous heart rhythms
        print(28)  # Attach Defib Pads
        continue

    # Stabilizing Measures
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Ongoing Monitoring and Responsive Actions
    if not (events[7] > 0.1):  # if breathing not already managed
        print(4)  # Examine Breathing
        continue

    # Continuously look for new data and re-assess situation
    print(16)  # View Monitor for updates

    # Check patient stability and finalize if stable
    if (sats is not None and sats >= 88 and 
        map_value is not None and map_value >= 60 and 
        resp_rate is not None and resp_rate >= 8):
        print(48)  # Finish Scenario
        break

    # Default action if no critical actions are required
    print(0)  # DoNothing, continue monitoring

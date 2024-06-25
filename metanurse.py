previous_actions = set()
while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate Response to Critical Conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        action = 17  # Start Chest Compression
    elif events[3] == 0:  # Airway not recently checked
        action = 3  # Examine Airway
    elif events[4] > 0.1 or events[5] > 0.1:  # Presence of Vomit or Blood
        action = 31  # Use Yankeur Suction Catheter
    elif events[7] > 0.1:  # Breathing None
        action = 29  # Use Bag Valve Mask
    elif events[17] > 0.1 or events[16] > 0.1:  # No palpable pulse
        action = 17  # Start Chest Compression
    elif events[28] > 0.1 or events[29] > 0.1 or events[30] > 0.1:  # Dangerous heart rhythms
        action = 28  # Attach Defib Pads
    elif sats is None or sats < 88:
        if sats is None and 'UseSatsProbe' not in previous_actions:
            action = 25  # Use Sats Probe
        else:
            action = 30  # Use Non Rebreather Mask
    elif map_value is None or map_value < 60:
        if map_value is None and 'UseBloodPressureCuff' not in previous_actions:
            action = 27  # Use Blood Pressure Cuff
        else:
            action = 15  # Give Fluids
    elif resp_rate is None or resp_rate < 8:
        if resp_rate is None and 'CheckRespirationRate' not in previous actions:
            action = 4  # Examine Breathing
        else:
            action = 29  # Use Bag Valve Mask
    else:
        if all([sats is not None and sats >= 88,
                map_value is not None and map_value >= 60,
                resp_rate is not None and resp_mark_rate >= 8]):
            action = 48  # Finish Scenario
        else:
            action = 16  # View Monitor for updates

    # Record used action if it's a monitoring or examining action
    if action in {25, 27, 4, 3, 16}:
        previous_actions.add(action)

    print(action)
    if action == 48:
        break
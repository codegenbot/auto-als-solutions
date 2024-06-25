while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Check for immediate life threats
    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # Start Chest Compression
        continue

    # ABCDE approach with proactive monitoring and actions
    if times[0] == 0:  # Initially or regularly check signs of life
        print(1)  # CheckSignsOfLife
        continue

    # Active management based on frequent examinations
    # Examine airway, breathing, circulation, disability, and exposure in a cycle

    # Airway examination
    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(3)  # Examine Airway
        continue

    # Airway management - if obstructions detected
    if events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:  # AirwayVomit, AirwayBlood, AirwayTongue
        print(31)  # Use Yankeur Suction Catheter
        continue

    # Use non-rebreather mask for oxygenation if sats are below 88 and above 65
    if sats is not None and 65 < sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue
    
    # Examine breathing if there are issues indicated
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue

    # Check circulation if not examined recently
    if times[4] == 0:  # MeasuredMAP not recently measured
        print(27)  # UseBloodPressureCuff
        continue

    # Manage circulation - fluids for low MAP
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Check respiratory rate and manage
    if resp_rate is not None and resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    # Reassess for stabilization: all conditions must be met and maintained
    if all([
        sats is not None and sats >= 88,
        map_value is not None and map_value >= 60,
        resp_rate is not None and resp_rate >= 8
    ]):
        print(25)  # UseSatsProbe to confirm
        continue

    # Default is to keep monitoring if none of the specific actions is required
    print(0)  # DoNothing
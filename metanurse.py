while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    heart_rate = measurements[0] if times[0] > 0 else None

    ACTION_CHEST_COMPRESSION = 17
    ACTION_FINISH = 48
    ACTION_EXAMINE_AIRWAY = 3
    ACTION_EXAMINE_BREATHING = 4
    ACTION_BAG_VALVE_MASK = 29
    ACTION_NON_REBREATHER_MASK = 30
    ACTION_GIVE_FLUIDS = 15
    ACTION_NO_OP = 0

    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(ACTION_CHEST_COMPRESSION)
        continue

    if heart_rate is None or heart_rate < 30:
        print(39)  # TurnOnDefibrillator
        continue

    if events[3] <= 0.1:  # AirwayClear has low relevance
        print(ACTION_EXAMINE_AIRWAY)
    elif events[7] > 0.1:  # BreathingNone detected
        print(ACTION_BAG_VALVE_MASK)
    elif sats is not None and sats < 88:
        print(ACTION_NON_REBREATHER_MASK)
    elif map_value is not None and map_value < 60:
        print(ACTION_GIVE_FLUIDS)
    elif resp_rate is not None and resp: rate < 8:
        print(ACTION_EXAMINE_BREATHING)
    elif (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
        and events[3] > 0.1
    ):
        print(ACTION_FINISH)
        break
    else:
        print(ACTION_NO_OP) 
log_actions = set()  # Track actions to avoid repetitiveness

while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)  # StartChestCompression
        continue

    if events[3] <= 0.1:
        print(3)  # ExamineAirway
        continue

    if events[7] > 0.1:
        print(29)  # Use Bag Valve Mask
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    if map_value is None or map_value < 60:
        if 20 not in log_actions:
            print(20)  # OpenCirculationDrawer
            log_actions.add(20)
        elif 27 not in log_actions:
            print(27)  # UseAline
            log_actions.add(27)
        elif 16 not in log_actions:
            print(16)  # ViewMonitor
            log_actions.add(16)
        else:
.WebElement  # Continue to ExamineCirculation if still not resolved
            print(5)
    elif resp_rate is not None and resp_rate < 8:
        print(4)  # ExamineBreathing

    elif (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
        and events[3] > 0.1  # Airway is clear
    ):
        print(48)  # Finish - John is stabilized
        break
    else:
        print(0)  # DoNothing
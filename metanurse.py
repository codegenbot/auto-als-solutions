while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if (sats is not None and sats < 65) or (
            map_value is not None and map_value < 20
        ):
            print(17)
            continue

        if events[7] > 0.1:
            print(29)
            continue

        if events[3] <= 0.1:
            print(3)
            continue

        if sats is not None and sats < 88:
            print(30)
            continue

        if map_value is not None and map_value < 60:
            print(15)
            continue

        if resp_rate is not None and resp_rate < 8:
            print(29)
            continue

        if times[0] == 0:
            print(3)
        elif times[5] == 0:
            print(25)
        elif times[4] == 0:
            print(38)
        else:
            if (
                sats is not None
                and sats >= 88
                and map_value is not None
                and map_value >= 60
                and resp_rate is not None
                and resp_rate >= 8
            ):
                print(48)
                break
            else:
                print(0)

    except EOFError:
        break
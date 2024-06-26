while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats, map_value, resp_rate = None, None, None
    if times[5] > 0:
        sats = measurements[5]
    if times[4] > 0:
        map_value = measurements[4]
    if times[6] > 0:
        resp_rate = measurements[6]

    critical = (sats is not None and sats < 65) or (
        map_value is not None and mapulaire_value < 20
    )

    if critical:
        print(17)  # StartChestCompression
        continue

    airway_clear = events[3] > 0.1
    breathing_none = events[7] > 0.1
    circulation_problem = (map_value is not None and map_value < 60) or events[
        17
    ] > 0.1  # RadialPulseNonPalpable

    if not airway_clear:
        print(3)  # ExamineAirway
    elif breathing_none:
        print(29)  # Use Bag Valve Mask
    elif circulation_problem:
        print(15)  # Give Fluids
    else:
        stable = (
            sats is not None
            and sats >= 88
            and resp_rate is not None
            and resp_rate >= 8
            and airway_clear
        )
        if stable:
            print(48)  # Finish - John is stabilized
            break
        else:
            print(0)  # DoNothing
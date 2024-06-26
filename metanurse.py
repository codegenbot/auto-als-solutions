assessment_cycle = 0
assessments = [3, 4, 5, 6, 7]
max_assessments = len(assessments)

while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        print(17)
        continue

    action = assessments[assessment_cycle % max_assessments]
    print(action)
    assessment_cycle += 1

    if sats is not None and map_value is not not None and resp_rate is not None:
        if sats >= 88 and map_value >= 60 and resp_rate >= 8:
            print(48)
            break
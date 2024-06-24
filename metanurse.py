import sys


def get_action(observations):
    global step
    step += 1

    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    cap_glucose = vital_signs_values[2] if vital_signs_time[2] > 0 else None
    temperature = vital_signs_values[3] if vital_signs_time[3] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None
    resps = vital_signs_values[6] if vital_signs_time[6] > 0 else None

    if step == 1:
        return 3
    if step == 2:
        return 4
    if step == 3:
        return 5

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17

    if events[7] > 0:
        return 29

    if map_value is not None and map_value < 60:
        return 15

    if sats is not None and sats < 88:
        return 30

    if step >= 4 and (map_value is None or resp_rate is None or sats is None):
        return 16

    if (
        all(v is not None and v >= 88 for v in [sats])
        and all(v is not None and v >= 8 for v in [resp_rate])
        and all(v is not None and v >= 60 for v in [map_value])
    ):
        return 48

    return 1


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
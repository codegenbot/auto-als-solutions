import sys

def get_action(observations):
    global step
    step += 1

    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if step == 1:
        return 3
    elif step == 2:
        return 35 if events[3] == 0 else 4
    elif step == 3:
        return 25
    elif step == 4:
        return 27
    elif step == 5:
        return 16
    
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17
    
    if events[8] > 0:
        return 29

    if sats is None or map_value is None or resp_rate is None:
        return 1

    if vital_signs_time[5] == 0:
        return 16

    if map_value and map_value < 60:
        return 15
    if resp_rate and resp_rate < 8:
        return 29
    if sats and sats < 88:
        return 30

    if map_value >= 60, resp_rate >= 8, sats >= 88:
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
import sys

def get_action(step, observations):
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
        return 4
    elif step == 3:
        return 5
    elif step == 4:
        return 6
    
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17
    
    if (sats is not None and sats >= 88) and (resp_rate is not None and resp_rate >= 8) and (map_value is not None and map_value >= 60):
        return 48

    if map_value is None:
        return 38
  
    if sats is not None and sats < 88:
        return 30

    if events[7] > 0 or events[8] > 0 or events[9] > 0:
        return 4

    if resp_rate is None or resp_rate < 8:
        return 4
    
    if resp_rate is not None and resp_rate >= 8 and events[3] == 0:
        return 3
    
    if map_value is not None and map_value < 60:
        return 15
    
    return 1

step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    step += 1
    action = get_action(step, input_data)
    print(action)
    if action == 48:
        break
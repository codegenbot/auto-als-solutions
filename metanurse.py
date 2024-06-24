import sys

def get_action(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if not events[3]:  
        return 3  
    if events[7] or events[8] or events[9]:  
        return 4  
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  
    if sats is None:  
        if vital_signs_time[5] == 0:
            return 25  
        return 16  
    if map_value is None:  
        if vital_signs_time[4] == 0:
            return 27  
        return 16  
    if sats < 88:
        return 30  
    if resp_rate is None:
        if vital_signs_time[1] == 0:
            return 4  
        return 16  
    if (resp_rate < 8) and (events[7] == 0):
        return 29  
    if (sats >= 88) and (resp_rate >= 8) and (map_value >= 60):
        return 48  
    return 1  

for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
import sys

def get_action(observations, prev_actions):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17

    if (sats is not None and sats >= 88) and (resp_rate is not None and resp_rate >= 8) and (map_value is not None and map_value >= 60):
        return 48

    if 'ExamineAirway' not in prev_actions:
        return 3
    
    if 'ExamineBreathing' not in prev_actions:
        return 4

    if 'UseSatsProbe' not in prev_actions and vital_signs_values[5] == 0:
        return 25

    if 'ViewMonitor' not in prev_actions and (vital_signs_time[1] == 0 or vital_signs_time[4] == 0 or vital_signs_time[5] == 0):
        return 16

    if resp_rate is not None and resp_rate < 8:
        return 28

    if map_value is None and vital_signs_time[4] == 0:
        return 27

    if sats is None:
        if vital_signs_time[5] == 0:
            return 25
        return 16
        
    if (sats is not None and sats < 88):
        return 30

    return 1

prev_actions = []
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data, prev_actions)
    print(action)
    prev_actions.append(action)
    if action == 48:
        break
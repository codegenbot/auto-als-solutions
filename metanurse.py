import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if state == 'start':
        return 8, 'response'
    elif state == 'response':
        return 3, 'airway'
    elif state == 'airway':
        return 4, 'breathing'
    elif state == 'breathing':
        return 5, 'circulation'
    elif state == 'circulation':
        return 6, 'disability'
    elif state == 'disability':
        return 7, 'exposure'
    elif state == 'exposure':
        return 25, 'sats_probe'
    elif state == 'sats_probe':
        return 27, 'bp_cuff'
    elif state == 'bp_cuff':
        return 16, 'monitor'
    elif state == 'monitor':
        sats = obs[52] if obs[45] > 0 else 0
        map_value = obs[51] if obs[44] > 0 else 0
        resp_rate = obs[53] if obs[46] > 0 else 0
        heart_rate = obs[47] if obs[40] > 0 else 0

        if sats < 0.65 or map_value < 20:
            return 17, 'cpr'
        elif sats < 0.88:
            return 30, 'oxygen'
        elif resp_rate < 8:
            return 29, 'ventilation'
        elif map_value < 60:
            return 15, 'fluids'
        elif heart_rate > 100:
            return 9, 'adenosine'
        elif sats >= 0.88 and resp_rate >= 8 and map_value >= 60:
            return 48, 'finish'
        else:
            return 16, 'monitor'
    elif state in ['oxygen', 'ventilation', 'fluids', 'adenosine', 'cpr']:
        return 16, 'monitor'
    else:
        return 16, 'monitor'

state = 'start'
for line in sys.stdin:
    action, new_state = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
    state = new_state
    if state == 'finish':
        break
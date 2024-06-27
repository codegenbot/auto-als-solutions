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
        return 16, 'monitor'
    elif state == 'monitor':
        if obs[38] == 0:
            return 25, 'sats_probe'
        elif obs[39] == 0:
            return 27, 'bp_cuff'
        else:
            return 38, 'check_bp'
    elif state in ['sats_probe', 'bp_cuff', 'check_bp']:
        return 16, 'assess'
    elif state == 'assess':
        if obs[51] == 0 or obs[52] < 8:
            return 29, 'assess'
        elif obs[50] < 0.88:
            return 30, 'assess'
        elif obs[52] < 60:
            return 15, 'assess'
        elif obs[50] < 0.65 or obs[52] < 20:
            return 17, 'cpr'
        elif obs[50] >= 0.88 and obs[51] >= 8 and obs[52] >= 60:
            return 48, 'finish'
        else:
            return 16, 'assess'
    
    return 0, state

state = 'start'
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
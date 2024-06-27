import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if obs[7] > 0 or obs[17] > 0:  # BreathingNone or RadialPulseNonPalpable
        return 17, 'cpr'
    
    if state == 'cpr':
        if obs[50] >= 0.65 and obs[52] >= 20:
            return 23, 'assess'
        return 17, 'cpr'
    
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
        if obs[51] < 8 or obs[50] < 0.88:
            return 30, 'oxygen'
        elif obs[52] < 60:
            return 15, 'fluids'
        elif obs[50] >= 0.88 and obs[51] >= 8 and obs[52] >= 60:
            return 48, 'finish'
        else:
            return 16, 'assess'
    elif state == 'oxygen':
        return 16, 'assess'
    elif state == 'fluids':
        return 16, 'assess'
    
    return 16, 'assess'

state = 'start'
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
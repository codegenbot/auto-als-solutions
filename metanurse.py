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
        return 25, 'sats_probe'
    elif state == 'sats_probe':
        return 27, 'bp_cuff'
    elif state == 'bp_cuff':
        return 38, 'check_bp'
    elif state == 'check_bp':
        return 16, 'assess'
    elif state == 'assess':
        if obs[17] > 0:  # RadialPulseNonPalpable
            return 17, 'cpr'
        if obs[50] < 0.65 or obs[52] < 20:
            return 17, 'cpr'
        if obs[51] == 0 or obs[52] < 8:
            return 29, 'assess'
        if obs[50] < 0.88:
            return 30, 'assess'
        if obs[52] < 60:
            return 15, 'fluids'
        if obs[44] > 100:  # High heart rate
            return 9, 'treat_tachycardia'
        if obs[50] >= 0.88 and obs[51] >= 8 and obs[52] >= 60:
            return 48, 'finish'
        return 16, 'assess'
    elif state == 'cpr':
        if obs[17] == 0:  # RadialPulsePalpable
            return 16, 'assess'
        return 17, 'cpr'
    elif state == 'fluids':
        return 15, 'assess'
    elif state == 'treat_tachycardia':
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
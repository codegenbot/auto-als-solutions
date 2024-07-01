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
        if obs[38] < 0.65 or obs[37] < 20:
            return 2, 'check_rhythm'
        elif obs[38] < 0.88:
            return 30, 'oxygen'
        elif obs[36] < 8:
            return 29, 'ventilation'
        elif obs[37] < 60:
            return 14, 'iv_access'
        elif obs[38] >= 0.88 and obs[36] >= 8 and obs[37] >= 60:
            return 48, 'finish'
        else:
            return 16, 'monitor'
    elif state == 'check_rhythm':
        return 17, 'cpr'
    elif state == 'cpr':
        return 2, 'check_rhythm_cpr'
    elif state == 'check_rhythm_cpr':
        return 23, 'resume_cpr'
    elif state == 'oxygen':
        return 16, 'monitor'
    elif state == 'ventilation':
        return 16, 'monitor'
    elif state == 'iv_access':
        return 15, 'fluids'
    elif state == 'fluids':
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
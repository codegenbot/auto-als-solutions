import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state, step_count):
    obs = parse_observations(observations)
    
    if step_count > 350:
        return 48, 'finish'

    if state == 'start':
        return 8, 'response'
    elif state == 'response':
        return 3, 'airway'
    elif state == 'airway':
        return 4, 'breathing'
    elif state == 'breathing':
        return 5, 'circulation'
    elif state == 'circulation':
        return 27, 'bp_cuff'
    elif state == 'bp_cuff':
        return 6, 'disability'
    elif state == 'disability':
        return 7, 'exposure'
    elif state == 'exposure':
        return 25, 'sats_probe'
    elif state == 'sats_probe':
        return 16, 'monitor'
    elif state == 'monitor':
        if obs[38] < 0.65 or obs[39] < 20:
            return 17, 'cpr'
        elif obs[35] == 0:
            return 29, 'bag_mask'
        elif obs[39] < 60:
            return 15, 'fluids'
        elif obs[38] < 0.88:
            return 30, 'oxygen'
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60 and obs[3] > 0:
            return 48, 'finish'
        else:
            return 2, 'check_rhythm'
    elif state == 'cpr':
        if step_count % 5 == 0:
            return 28, 'attach_defib'
        elif step_count % 5 == 1:
            return 39, 'turn_on_defib'
        elif step_count % 5 == 2:
            return 40, 'charge_defib'
        elif step_count % 5 == 3:
            return 2, 'check_rhythm'
        else:
            return 17, 'cpr'
    elif state == 'check_rhythm':
        if obs[32] > 0:  # VF
            return 41, 'defib'
        elif obs[31] > 0:  # VT
            return 41, 'defib'
        elif obs[29] > 0:  # SVT
            return 9, 'give_adenosine'
        elif obs[30] > 0:  # AF
            return 11, 'give_amiodarone'
        else:
            return 10, 'give_adrenaline'
    elif state == 'bag_mask':
        return 16, 'monitor'
    elif state == 'fluids':
        return 16, 'monitor'
    elif state == 'oxygen':
        return 16, 'monitor'
    
    return 0, state

state = 'start'
step_count = 0
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state, step_count)
    print(action)
    sys.stdout.flush()
    step_count += 1
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
        if obs[7] > 0.5 or obs[8] > 0.5 or obs[9] > 0.5:  # No breathing or abnormal breathing
            return 29, 'bag_mask'
        else:
            return 5, 'circulation'
    elif state == 'bag_mask':
        return 5, 'circulation'
    elif state == 'circulation':
        return 27, 'bp_cuff'
    elif state == 'bp_cuff':
        return 25, 'sats_probe'
    elif state == 'sats_probe':
        return 16, 'monitor'
    elif state == 'monitor':
        if obs[38] < 0.65 or obs[39] < 20:
            return 17, 'cpr'
        elif obs[35] == 0:  # No breathing
            return 29, 'monitor'
        elif obs[39] < 60:
            return 15, 'monitor'
        elif obs[38] < 0.88:
            return 30, 'monitor'
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'
        else:
            return 16, 'monitor'
    elif state == 'cpr':
        return 2, 'check_rhythm'
    elif state == 'check_rhythm':
        if obs[32] > 0.5 or obs[38] > 0.5:  # VF or VT
            return 40, 'charge_defib'
        else:
            return 10, 'give_adrenaline'
    elif state == 'charge_defib':
        return 28, 'attach_pads'
    elif state == 'attach_pads':
        return 39, 'shock'
    elif state == 'shock':
        return 23, 'cpr'
    elif state == 'give_adrenaline':
        return 23, 'cpr'
    
    return 0, state

state = 'start'
steps = 0
while steps < 350:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
    steps += 1
    if action == 48:  # Finish
        break

if steps == 350:
    print(48)  # Finish if step limit reached
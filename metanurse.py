import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def is_cardiac_arrest(obs):
    return obs[38] < 0.65 or obs[37] < 20 or obs[37] == 0

def is_shockable_rhythm(obs):
    return obs[32] > 0 or obs[38] > 0  # VT or VF

def is_stabilized(obs):
    return obs[38] >= 0.88 and obs[36] >= 8 and obs[37] >= 60

def choose_action(observations, state, steps):
    obs = parse_observations(observations)
    
    if steps > 350:
        return 48, 'finish'

    if is_cardiac_arrest(obs):
        if state != 'cpr':
            return 17, 'cpr'
        elif state == 'cpr':
            if steps % 5 == 0:
                return 2, 'check_rhythm_cpr'
            else:
                return 23, 'resume_cpr'
    
    if state == 'check_rhythm_cpr':
        if is_shockable_rhythm(obs):
            return 28, 'attach_defib_pads'
        else:
            return 10, 'give_adrenaline'

    if state == 'attach_defib_pads':
        return 39, 'turn_on_defib'
    
    if state == 'turn_on_defib':
        return 40, 'charge_defib'
    
    if state == 'charge_defib':
        return 0, 'shock'

    if state == 'shock':
        return 23, 'resume_cpr'

    if state == 'give_adrenaline':
        return 23, 'resume_cpr'

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
        if obs[38] < 0.88:
            return 30, 'oxygen'
        elif obs[36] < 8:
            return 29, 'ventilation'
        elif obs[37] < 60:
            return 14, 'iv_access'
        elif is_stabilized(obs):
            return 48, 'finish'
        else:
            return 16, 'monitor'
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
steps = 0
for line in sys.stdin:
    steps += 1
    action, new_state = choose_action(line.strip(), state, steps)
    print(action)
    sys.stdout.flush()
    state = new_state
    if state == 'finish':
        break
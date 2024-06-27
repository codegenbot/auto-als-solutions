import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state, step_count, cpr_count, last_adrenaline):
    obs = parse_observations(observations)
    
    if step_count > 350:
        return 48, 'finish', cpr_count, last_adrenaline

    if state == 'start':
        return 8, 'response', cpr_count, last_adrenaline
    elif state == 'response':
        return 3, 'airway', cpr_count, last_adrenaline
    elif state == 'airway':
        return 4, 'breathing', cpr_count, last_adrenaline
    elif state == 'breathing':
        return 25, 'sats_probe', cpr_count, last_adrenaline
    elif state == 'sats_probe':
        return 27, 'bp_cuff', cpr_count, last_adrenaline
    elif state == 'bp_cuff':
        return 16, 'monitor', cpr_count, last_adrenaline
    elif state == 'monitor':
        if obs[39] == 0 or obs[38] < 0.65:
            return 17, 'cpr', 0, step_count
        elif obs[39] < 60 and obs[39] > 20:
            return 15, 'fluids', cpr_count, last_adrenaline
        elif obs[38] < 0.88 and obs[38] >= 0.65:
            return 30, 'oxygen', cpr_count, last_adrenaline
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60 and obs[3] > 0:
            return 48, 'finish', cpr_count, last_adrenaline
        else:
            return 2, 'check_rhythm', cpr_count, last_adrenaline
    elif state == 'cpr':
        cpr_count += 1
        if cpr_count % 30 == 0:
            return 22, 'bag_cpr', cpr_count, last_adrenaline
        elif cpr_count % 150 == 0 or (cpr_count == 1 and step_count - last_adrenaline >= 180):
            return 10, 'give_adrenaline', cpr_count, step_count
        elif cpr_count % 60 == 0:
            return 2, 'check_rhythm', cpr_count, last_adrenaline
        else:
            return 17, 'cpr', cpr_count, last_adrenaline
    elif state == 'check_rhythm':
        if obs[38] > 0:  # VF
            return 28, 'attach_defib', cpr_count, last_adrenaline
        elif obs[32] > 0:  # VT
            return 28, 'attach_defib', cpr_count, last_adrenaline
        else:
            return 16, 'monitor', cpr_count, last_adrenaline
    elif state == 'attach_defib':
        return 39, 'turn_on_defib', cpr_count, last_adrenaline
    elif state == 'turn_on_defib':
        return 40, 'charge_defib', cpr_count, last_adrenaline
    elif state == 'charge_defib':
        return 41, 'shock', cpr_count, last_adrenaline
    elif state == 'shock':
        return 17, 'cpr', cpr_count, last_adrenaline
    elif state == 'bag_cpr':
        return 17, 'cpr', cpr_count, last_adrenaline
    elif state == 'give_adrenaline':
        return 17, 'cpr', cpr_count, last_adrenaline
    elif state == 
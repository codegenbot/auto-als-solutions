import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    def check_vitals():
        breathing = obs[35] if obs[34] > 0 else 0
        sats = obs[39] if obs[38] > 0 else 0
        map_value = obs[40] if obs[39] > 0 else 0
        return breathing, sats, map_value

    def is_stable(breathing, sats, map_value):
        return breathing >= 8 and sats >= 0.88 and map_value >= 60

    breathing, sats, map_value = check_vitals()

    if state == 'start':
        return 8, 'response'
    elif state == 'response':
        return 3, 'airway'
    elif state == 'airway':
        return 4, 'breathing'
    elif state == 'breathing':
        return 29, 'bag_mask'
    elif state == 'bag_mask':
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
        if sats < 0.65 or map_value < 20:
            return 1, 'cardiac_arrest'
        elif breathing == 0:
            return 29, 'monitor'
        elif map_value < 60:
            return 15, 'monitor'
        elif sats < 0.88:
            return 30, 'monitor'
        elif is_stable(breathing, sats, map_value):
            return 48, 'finish'
        else:
            return 16, 'monitor'
    elif state == 'cardiac_arrest':
        return 17, 'cpr'
    elif state == 'cpr':
        if sats >= 0.65 and map_value >= 20:
            return 16, 'monitor'
        else:
            return 2, 'check_rhythm'
    elif state == 'check_rhythm':
        if obs[32] > 0:  # VF rhythm
            return 28, 'attach_pads'
        else:
            return 10, 'give_adrenaline'
    elif state == 'attach_pads':
        return 39, 'charge_defib'
    elif state == 'charge_defib':
        return 40, 'shock'
    elif state == 'shock':
        return 23, 'cpr'
    elif state == 'give_adrenaline':
        return 23, 'cpr'
    
    return 0, state

state = 'start'
step_count = 0
while step_count < 350:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
    if action == 48:  # Finish action
        break
    step_count += 1

if step_count >= 350:
    print(48)  # Finish if step limit reached
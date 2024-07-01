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
        if obs[7] > 0:  # BreathingNone event
            return 17, 'start_cpr'
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
            return 28, 'attach_defib_pads'
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
    elif state == 'attach_defib_pads':
        return 39, 'turn_on_defib'
    elif state == 'turn_on_defib':
        return 2, 'check_rhythm'
    elif state == 'check_rhythm':
        if obs[38] > 0 or obs[32] > 0:  # VF or VT
            return 40, 'charge_defib'
        return 17, 'start_cpr'
    elif state == 'charge_defib':
        return 41, 'shock'
    elif state == 'shock':
        return 17, 'start_cpr'
    elif state == 'start_cpr':
        return 17, 'cpr_cycle'
    elif state == 'cpr_cycle':
        state['compressions'] = state.get('compressions', 0) + 1
        if state['compressions'] < 30:
            return 17, 'cpr_cycle'
        return 22, 'ventilate'
    elif state == 'ventilate':
        state['ventilations'] = state.get('ventilations', 0) + 1
        if state['ventilations'] < 2:
            return 22, 'ventilate'
        state['compressions'] = 0
        state['ventilations'] = 0
        state['cycles'] = state.get('cycles', 0) + 1
        if state['cycles'] % 5 == 0:
            return 10, 'give_adrenaline'
        return 2, 'check_rhythm'
    elif state == 'give_adrenaline':
        state['adrenaline_given'] = True
        return 17, 'start_cpr'
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

state = {'start': True}
for line in sys.stdin:
    action, new_state = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
    state = {'state': new
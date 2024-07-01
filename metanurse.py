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
        if obs[7] > 0.5:  # BreathingNone event
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
        else:
            return 17, 'start_cpr'
    elif state == 'charge_defib':
        return 41, 'shock'
    elif state == 'shock':
        return 17, 'start_cpr'
    elif state == 'start_cpr':
        return 17, 'cpr_cycle'
    elif state == 'cpr_cycle':
        state['compressions'] = state.get('compressions', 0) + 1
        if state['compressions'] == 30:
            return 22, 'ventilate'
        else:
            return 17, 'cpr_cycle'
    elif state == 'ventilate':
        state['ventilations'] = state.get('ventilations', 0) + 1
        if state['ventilations'] == 2:
            state['compressions'] = 0
            state['ventilations'] = 0
            state['cycles'] = state.get('cycles', 0) + 1
            if state['cycles'] % 2 == 0:
                return 10, 'give_adrenaline'
            else:
                return 2, 'check_rhythm'
        else:
            return 22, 'ventilate'
    elif state == 'give_adrenaline':
        if state['cycles'] == 6:
            return 11, 'give_amiodarone'
        else:
            return 17, 'start_cpr'
    elif state == 'give_amiodarone':
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
        return 
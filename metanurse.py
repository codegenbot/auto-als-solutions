import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if obs[38] < 0.65 or obs[39] < 20:
        return 17, 'cpr'  # StartChestCompression
    
    if state == 'start':
        return 8, 'response'  # ExamineResponse
    elif state == 'response':
        return 3, 'airway'  # ExamineAirway
    elif state == 'airway':
        return 4, 'breathing'  # ExamineBreathing
    elif state == 'breathing':
        return 5, 'circulation'  # ExamineCirculation
    elif state == 'circulation':
        return 6, 'disability'  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure'  # ExamineExposure
    elif state == 'exposure':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        if obs[38] == 0:
            return 25, 'sats_probe'  # UseSatsProbe
        elif obs[39] == 0:
            return 27, 'bp_cuff'  # UseBloodPressureCuff
        else:
            return 38, 'check_bp'  # TakeBloodPressure
    elif state == 'sats_probe':
        return 27, 'bp_cuff'  # UseBloodPressureCuff
    elif state in ['bp_cuff', 'check_bp']:
        return 16, 'assess'  # ViewMonitor
    elif state == 'assess':
        if obs[35] == 0:  # No breathing
            return 29, 'bag_valve_mask'  # UseBagValveMask
        elif obs[38] < 0.88:
            return 30, 'non_rebreather'  # UseNonRebreatherMask
        elif obs[39] < 60:
            return 15, 'fluids'  # GiveFluids
        elif obs[33] > 100:  # High heart rate
            return 2, 'check_rhythm'  # CheckRhythm
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'assess'  # ViewMonitor
    elif state == 'bag_valve_mask':
        return 16, 'assess'  # ViewMonitor
    elif state == 'non_rebreather':
        return 16, 'assess'  # ViewMonitor
    elif state == 'fluids':
        if obs[39] < 40:
            return 10, 'adrenaline'  # GiveAdrenaline
        else:
            return 16, 'assess'  # ViewMonitor
    elif state == 'adrenaline':
        return 16, 'assess'  # ViewMonitor
    elif state == 'check_rhythm':
        if obs[32] > 0 or obs[38] > 0:  # VF or VT
            return 28, 'attach_defib'  # AttachDefibPads
        else:
            return 16, 'assess'  # ViewMonitor
    elif state == 'attach_defib':
        return 39, 'turn_on_defib'  # TurnOnDefibrillator
    elif state == 'turn_on_defib':
        return 40, 'charge_defib'  # DefibrillatorCharge
    elif state == 'charge_defib':
        return 2, 'shock'  # CheckRhythm
    elif state == 'shock':
        return 16, 'assess'  # ViewMonitor
    elif state == 'cpr':
        return 16, 'assess'  # ViewMonitor
    
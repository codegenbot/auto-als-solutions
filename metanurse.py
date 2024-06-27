import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state, step_count):
    obs = parse_observations(observations)
    
    # Check for cardiac arrest
    if obs[38] < 0.65 or obs[39] < 20:
        return 17, 'cpr', step_count + 1  # StartChestCompression
    
    if state == 'start':
        return 8, 'response', step_count + 1  # ExamineResponse
    elif state == 'response':
        return 3, 'airway', step_count + 1  # ExamineAirway
    elif state == 'airway':
        return 4, 'breathing', step_count + 1  # ExamineBreathing
    elif state == 'breathing':
        return 5, 'circulation', step_count + 1  # ExamineCirculation
    elif state == 'circulation':
        return 6, 'disability', step_count + 1  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure', step_count + 1  # ExamineExposure
    elif state == 'exposure':
        return 16, 'monitor', step_count + 1  # ViewMonitor
    elif state == 'monitor':
        if obs[38] == 0:
            return 25, 'sats_probe', step_count + 1  # UseSatsProbe
        elif obs[39] == 0:
            return 27, 'bp_cuff', step_count + 1  # UseBloodPressureCuff
        else:
            return 38, 'check_bp', step_count + 1  # TakeBloodPressure
    elif state == 'sats_probe':
        return 27, 'bp_cuff', step_count + 1  # UseBloodPressureCuff
    elif state in ['bp_cuff', 'check_bp']:
        return 16, 'assess', step_count + 1  # ViewMonitor
    elif state == 'assess':
        if obs[35] == 0:  # No breathing
            return 29, 'bag_mask', step_count + 1  # UseBagValveMask
        elif obs[38] < 0.88:
            return 30, 'oxygen', step_count + 1  # UseNonRebreatherMask
        elif obs[39] < 60:
            return 15, 'fluids', step_count + 1  # GiveFluids
        elif obs[33] > 0 or obs[34] > 0:  # Check for tachycardia
            return 2, 'check_rhythm', step_count + 1  # CheckRhythm
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish', step_count + 1  # Finish
        else:
            return 16, 'assess', step_count + 1  # ViewMonitor
    elif state == 'cpr':
        return 28, 'defib_pads', step_count + 1  # AttachDefibPads
    elif state == 'defib_pads':
        return 39, 'turn_on_defib', step_count + 1  # TurnOnDefibrillator
    elif state == 'turn_on_defib':
        return 40, 'charge_defib', step_count + 1  # DefibrillatorCharge
    elif state == 'charge_defib':
        return 2, 'check_rhythm', step_count + 1  # CheckRhythm
    elif state == 'check_rhythm':
        if obs[38] > 0:  # VF detected
            return 41, 'shock', step_count + 1  # DefibrillatorCurrentUp
        else:
            return 23, 'resume_cpr', step_count + 1  # ResumeCPR
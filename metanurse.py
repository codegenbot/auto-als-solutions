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
            return 29, 'bag_valve'  # UseBagValveMask
        elif obs[38] < 0.88:
            return 30, 'oxygen'  # UseNonRebreatherMask
        elif obs[39] < 60:
            return 15, 'fluids'  # GiveFluids
        elif obs[33] > 100:  # Tachycardia
            return 2, 'check_rhythm'  # CheckRhythm
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'assess'  # ViewMonitor
    elif state == 'bag_valve':
        return 16, 'assess'  # ViewMonitor
    elif state == 'oxygen':
        return 16, 'assess'  # ViewMonitor
    elif state == 'fluids':
        if obs[39] < 40:
            return 10, 'adrenaline'  # GiveAdrenaline
        else:
            return 16, 'assess'  # ViewMonitor
    elif state == 'adrenaline':
        return 16, 'assess'  # ViewMonitor
    elif state == 'check_rhythm':
        if obs[32] > 0 or obs[37] > 0 or obs[38] > 0:  # VF, VT, or Torsades
            return 28, 'defib_pads'  # AttachDefibPads
        else:
            return 16, 'assess'  # ViewMonitor
    elif state == 'defib_pads':
        return 39, 'defib_on'  # TurnOnDefibrillator
    elif state == 'defib_on':
        return 40, 'defib_charge'  # DefibrillatorCharge
    elif state == 'defib_charge':
        return 2, 'assess'  # CheckRhythm
    elif state == 'cpr':
        return 2, 'assess'  # CheckRhythm
    
    return 0, state  # DoNothing

state = 'start'

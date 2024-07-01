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
        return 5, 'circulation'
    elif state == 'circulation':
        return 6, 'disability'
    elif state == 'disability':
        return 7, 'exposure'
    elif state == 'exposure':
        return 25, 'sats_probe'  # UseSatsProbe
    elif state == 'sats_probe':
        return 27, 'bp_cuff'  # UseBloodPressureCuff
    elif state == 'bp_cuff':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        if obs[38] < 0.65 or obs[37] < 20:
            return 2, 'check_rhythm'  # CheckRhythm
        elif obs[38] < 0.88:
            return 30, 'oxygen'  # UseNonRebreatherMask
        elif obs[36] < 8:
            return 29, 'ventilation'  # UseBagValveMask
        elif obs[37] < 60:
            return 14, 'iv_catheter'  # UseVenflonIVCatheter
        elif obs[38] >= 0.88 and obs[36] >= 8 and obs[37] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 8, 'reassess'  # Start reassessment
    elif state == 'check_rhythm':
        return 17, 'cpr'  # StartChestCompression
    elif state == 'oxygen':
        return 16, 'monitor'
    elif state == 'ventilation':
        return 16, 'monitor'
    elif state == 'iv_catheter':
        return 15, 'fluids'  # GiveFluids
    elif state == 'fluids':
        return 16, 'monitor'
    elif state == 'reassess':
        return 3, 'airway'  # Start ABCDE assessment again
    elif state == 'cpr':
        return 2, 'check_rhythm'
    else:
        return 16, 'monitor'

state = 'start'
for line in sys.stdin:
    action, new_state = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
    state = new_state
    if state == 'finish':
        break
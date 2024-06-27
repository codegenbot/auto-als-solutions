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
        if obs[35] == 0:  # No breathing
            return 29, 'bag_mask'  # UseBagValveMask
        return 5, 'circulation'  # ExamineCirculation
    elif state == 'circulation':
        return 27, 'bp_cuff'  # UseBloodPressureCuff
    elif state == 'bp_cuff':
        return 25, 'sats_probe'  # UseSatsProbe
    elif state == 'sats_probe':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        if obs[39] < 60 and obs[39] >= 20:
            return 15, 'fluids'  # GiveFluids
        elif obs[38] < 0.88 and obs[38] >= 0.65:
            return 30, 'oxygen'  # UseNonRebreatherMask
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 6, 'disability'  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure'  # ExamineExposure
    elif state == 'exposure':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'fluids' or state == 'oxygen':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'cpr':
        return 2, 'check_rhythm'  # CheckRhythm
    elif state == 'check_rhythm':
        return 10, 'give_adrenaline'  # GiveAdrenaline
    elif state == 'give_adrenaline':
        return 16, 'monitor'  # ViewMonitor after CPR
    
    return 16, 'monitor'  # Default to ViewMonitor

state = 'start'
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
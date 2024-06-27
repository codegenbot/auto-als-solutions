import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if state == 'start':
        return 8, 'response'  # ExamineResponse
    elif state == 'response':
        return 3, 'airway'  # ExamineAirway
    elif state == 'airway':
        return 4, 'breathing'  # ExamineBreathing
    elif state == 'breathing':
        return 25, 'sats_probe'  # UseSatsProbe
    elif state == 'sats_probe':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        if obs[35] == 0 or obs[39] == 0:  # No breathing or MAP is 0
            return 17, 'cpr'  # StartChestCompression
        elif obs[38] < 0.88 and obs[35] > 0:
            return 30, 'use_mask'  # UseNonRebreatherMask
        elif obs[39] < 60:
            return 14, 'venflonIV'  # UseVenflonIVCatheter
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 5, 'circulation'  # ExamineCirculation
    elif state == 'use_mask':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'venflonIV':
        return 15, 'give_fluids'  # GiveFluids
    elif state == 'give_fluids':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'circulation':
        return 27, 'bp_cuff'  # UseBloodPressureCuff
    elif state == 'bp_cuff':
        return 6, 'disability'  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure'  # ExamineExposure
    elif state == 'exposure':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'cpr':
        return 2, 'check_rhythm'  # CheckRhythm
    elif state == 'check_rhythm':
        return 10, 'give_adrenaline'  # GiveAdrenaline
    elif state == 'give_adrenaline':
        return 23, 'resume_cpr'  # ResumeCPR
    elif state == 'resume_cpr':
        return 16, 'monitor'  # ViewMonitor
    
    return 0, state  # DoNothing

state = 'start'
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
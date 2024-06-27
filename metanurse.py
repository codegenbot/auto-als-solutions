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
        return 29, 'bag_mask'  # UseBagValveMask
    elif state == 'bag_mask':
        return 5, 'circulation'  # ExamineCirculation
    elif state == 'circulation':
        return 27, 'bp_cuff'  # UseBloodPressureCuff
    elif state == 'bp_cuff':
        return 6, 'disability'  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure'  # ExamineExposure
    elif state == 'exposure':
        return 25, 'sats_probe'  # UseSatsProbe
    elif state == 'sats_probe':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        if obs[38] < 0.65 or obs[39] < 20:
            return 17, 'cpr'  # StartChestCompression
        elif obs[35] < 8:
            return 29, 'monitor'  # UseBagValveMask
        elif obs[38] < 0.88:
            return 30, 'monitor'  # UseNonRebreatherMask
        elif obs[39] < 60:
            return 15, 'monitor'  # GiveFluids
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'monitor'  # ViewMonitor
    elif state == 'cpr':
        return 23, 'monitor'  # ResumeCPR
    
    return 16, 'monitor'  # ViewMonitor

state = 'start'
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
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
        return 6, 'disability'  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure'  # ExamineExposure
    elif state == 'exposure':
        return 25, 'sats_probe'  # UseSatsProbe
    elif state == 'sats_probe':
        return 16, 'monitor'  # ViewMonitor
    elif state in ['monitor', 'bag_mask', 'cpr']:
        if obs[35] == 0:  # No breathing
            return 29, 'bag_mask'  # UseBagValveMask
        elif 20 <= obs[39] < 60:
            return 15, 'monitor'  # GiveFluids
        elif 0.65 <= obs[38] < 0.88:
            return 30, 'monitor'  # UseNonRebreatherMask
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'monitor'  # ViewMonitor again
    
    return 16, 'monitor'  # Default action: ViewMonitor

state = 'start'
while True:
    try:
        observations = input().strip()
        if not observations:
            break
        action, state = choose_action(observations, state)
        print(action)
        sys.stdout.flush()
    except EOFError:
        break
    except Exception as e:
        print(16)  # ViewMonitor as default action in case of unexpected error
        sys.stdout.flush()
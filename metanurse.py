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
        elif obs[37] == 0:
            return 27, 'bp_cuff'  # UseBloodPressureCuff
        else:
            return 16, 'stabilize'  # ViewMonitor
    elif state == 'sats_probe':
        return 27, 'bp_cuff'  # UseBloodPressureCuff
    elif state == 'bp_cuff':
        return 16, 'stabilize'  # ViewMonitor
    elif state == 'stabilize':
        if obs[38] < 0.88:
            return 30, 'stabilize'  # UseNonRebreatherMask
        elif obs[36] < 8:
            return 29, 'stabilize'  # UseBagValveMask
        elif obs[37] < 60:
            return 15, 'stabilize'  # GiveFluids
        elif obs[38] >= 0.88 and obs[36] >= 8 and obs[37] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'stabilize'  # ViewMonitor
    
    return 0, state  # DoNothing

state = 'start'
for line in sys.stdin:
    action, new_state = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
    state = new_state
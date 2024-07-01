import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state, action_counts):
    if obs[7] > 0:  # BreathingNone detected
        if action_counts['UseBagValveMask'] < 3:
            action_counts['UseBagValveMask'] += 1
            return 29, state, action_counts  # UseBagValveMask
        elif obs[16] == 0 and obs[17] == 0:
            return 5, 'circulation', action_counts  # ExamineCirculation
        elif obs[40] == 0:
            return 25, state, action_counts  # UseSatsProbe
        elif obs[39] == 0:
            return 27, state, action_counts  # UseBloodPressureCuff
    
    if state == 'start':
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            return 8, 'airway', action_counts  # ExamineResponse
    elif state == 'airway':
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            return 3, 'breathing', action_counts  # ExamineAirway
    elif state == 'breathing':
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            return 4, 'circulation', action_counts  # ExamineBreathing
    elif state == 'circulation':
        if obs[16] == 0 and obs[17] == 0:
            return 5, 'disability', action_counts  # ExamineCirculation
    elif state == 'disability':
        if obs[23] == 0 and obs[24] == 0:
            return 6, 'exposure', action_counts  # ExamineDisability
    elif state == 'exposure':
        if obs[25] == 0 and obs[26] == 0:
            return 7, 'monitor', action_counts  # ExamineExposure
    elif state == 'monitor':
        if obs[39] == 0:
            return 27, state, action_counts  # UseBloodPressureCuff
        elif obs[40] == 0:
            return 25, state, action_counts  # UseSatsProbe
        else:
            return 16, 'treat', action_counts  # ViewMonitor
    elif state == 'treat':
        if obs[46] < 88 and obs[40] > 0:
            if action_counts['UseNonRebreatherMask'] < 3:
                action_counts['UseNonRebreatherMask'] += 1
                return 30, state, action_counts  # UseNonRebreatherMask
        elif obs[45] < 60 and obs[39] > 0:
            if action_counts['GiveFluids'] < 3:
                action_counts['GiveFluids'] += 1
                return 15, state, action_counts  # GiveFluids
        elif obs[46] >= 88 and obs[45] >= 60:
            return 48, 'finish', action_counts  # Finish
    
    return 16, state, action_counts  # ViewMonitor as default action

state = 'start'
action_counts = {'UseBagValveMask': 0, 'UseNonRebreatherMask': 0, 'GiveFluids': 0}

for step in range(350):
    observations = input()
    obs = parse_observations(observations)
    action, state, action_counts = choose_action(obs, state, action_counts)
    print(action)
    sys.stdout.flush()
    if action == 48:
        break
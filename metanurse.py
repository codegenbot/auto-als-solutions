import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state, action_counts):
    if action_counts[state] > 5:
        state = (state + 1) % 5

    if state == 0:  # Airway
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            action_counts[0] += 1
            return 8, state  # ExamineResponse
        if obs[7] > 0:  # BreathingNone detected
            state = 1
        elif obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            action_counts[0] += 1
            return 3, state  # ExamineAirway
        else:
            state = 1
    
    if state == 1:  # Breathing
        if obs[7] > 0:  # BreathingNone
            action_counts[1] += 1
            return 29, state  # UseBagValveMask
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            action_counts[1] += 1
            return 4, state  # ExamineBreathing
        else:
            state = 2

    if state == 2:  # Circulation
        if obs[16] == 0 and obs[17] == 0:
            action_counts[2] += 1
            return 5, state  # ExamineCirculation
        if obs[39] == 0:
            action_counts[2] += 1
            return 27, state  # UseBloodPressureCuff
        if obs[40] == 0:
            action_counts[2] += 1
            return 25, state  # UseSatsProbe
        else:
            state = 3

    if state == 3:  # Disability
        if obs[23] == 0 and obs[24] == 0:
            action_counts[3] += 1
            return 6, state  # ExamineDisability
        else:
            state = 4

    if state == 4:  # Exposure
        if obs[25] == 0 and obs[26] == 0:
            action_counts[4] += 1
            return 7, state  # ExamineExposure
        else:
            state = 0

    if obs[46] < 88 and obs[40] > 0:
        return 30, state  # UseNonRebreatherMask
    if obs[45] < 60 and obs[39] > 0:
        return 15, state  # GiveFluids

    if obs[46] >= 88 and obs[45] >= 60 and obs[41] >= 8:
        return 48, state  # Finish

    return 0, state  # DoNothing

state = 0
action_counts = [0, 0, 0, 0, 0]

for step in range(350):
    observations = input()
    obs = parse_observations(observations)
    action, state = choose_action(obs, state, action_counts)
    print(action)
    sys.stdout.flush()
    if action == 48:
        break
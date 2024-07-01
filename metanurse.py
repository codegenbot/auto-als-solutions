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
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            action_counts[0] += 1
            return 3, state  # ExamineAirway
        state = 1

    if state == 1:  # Breathing
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            action_counts[1] += 1
            return 4, state  # ExamineBreathing
        if obs[40] == 0:
            action_counts[1] += 1
            return 25, state  # UseSatsProbe
        state = 2

    if state == 2:  # Circulation
        if obs[16] == 0 and obs[17] == 0:
            action_counts[2] += 1
            return 5, state  # ExamineCirculation
        if obs[39] == 0:
            action_counts[2] += 1
            return 27, state  # UseBloodPressureCuff
        state = 3

    if state == 3:  # Disability
        if obs[23] == 0 and obs[24] == 0:
            action_counts[3] += 1
            return 6, state  # ExamineDisability
        state = 4

    if state == 4:  # Exposure
        if obs[25] == 0 and obs[26] == 0:
            action_counts[4] += 1
            return 7, state  # ExamineExposure
        state = 0

    if obs[46] < 65 or obs[45] < 20:
        return 17, state  # StartChestCompression

    if obs[40] > 0 and obs[46] < 88:
        return 30, state  # UseNonRebreatherMask

    if obs[39] > 0 and obs[45] < 60:
        if obs[14] == 0:
            return 14, state  # UseVenflonIVCatheter
        return 15, state  # GiveFluids

    if obs[39] > 0 or obs[40] > 0:
        return 16, state  # ViewMonitor

    if obs[3] > 0 and obs[46] >= 88 and obs[41] >= 8 and obs[45] >= 60:
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
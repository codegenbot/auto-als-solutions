import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state, action_counts, actions_taken):
    if state == 0:  # Initial setup
        if 25 not in actions_taken:
            actions_taken.add(25)
            return 25, state  # UseSatsProbe
        if 27 not in actions_taken:
            actions_taken.add(27)
            return 27, state  # UseBloodPressureCuff
        if 14 not in actions_taken:
            actions_taken.add(14)
            return 14, state  # UseVenflonIVCatheter
        state = 1

    if state == 1:  # ABCDE assessment
        if action_counts[state] > 5:
            state = (state + 1) % 6

        if state == 1:  # Airway
            if 8 not in actions_taken:
                actions_taken.add(8)
                return 8, state  # ExamineResponse
            if 3 not in actions_taken:
                actions_taken.add(3)
                return 3, state  # ExamineAirway
            state = 2

        elif state == 2:  # Breathing
            if 4 not in actions_taken:
                actions_taken.add(4)
                return 4, state  # ExamineBreathing
            state = 3

        elif state == 3:  # Circulation
            if 5 not in actions_taken:
                actions_taken.add(5)
                return 5, state  # ExamineCirculation
            state = 4

        elif state == 4:  # Disability
            if 6 not in actions_taken:
                actions_taken.add(6)
                return 6, state  # ExamineDisability
            state = 5

        elif state == 5:  # Exposure
            if 7 not in actions_taken:
                actions_taken.add(7)
                return 7, state  # ExamineExposure
            state = 1

    # Check vital signs
    if 16 not in actions_taken:
        actions_taken.add(16)
        return 16, state  # ViewMonitor

    # Handle critical conditions
    if obs[46] < 65 or obs[45] < 20:
        return 17, state  # StartChestCompression

    # Stabilize patient
    if obs[46] < 88 and 30 not in actions_taken:
        actions_taken.add(30)
        return 30, state  # UseNonRebreatherMask
    if obs[45] < 60 and 15 not in actions_taken:
        actions_taken.add(15)
        return 15, state  # GiveFluids

    # Check if patient is stable
    if obs[46] >= 88 and obs[45] >= 60 and obs[41] >= 8 and obs[3] > 0:
        return 48, state  # Finish

    action_counts[state] += 1
    return 0, state  # DoNothing

state = 0
action_counts = [0, 0, 0, 0, 0, 0]
actions_taken = set()

for step in range(350):
    observations = input()
    obs = parse_observations(observations)
    action, state = choose_action(obs, state, action_counts, actions_taken)
    print(action)
    sys.stdout.flush()
    if action == 48:
        break
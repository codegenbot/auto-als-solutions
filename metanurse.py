import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if state['step'] == 0:
        state['step'] += 1
        return 1, state  # CheckSignsOfLife

    if state['step'] == 1:
        state['step'] += 1
        return 8, state  # ExamineResponse

    if state['step'] == 2:
        state['step'] += 1
        return 3, state  # ExamineAirway

    if state['step'] == 3:
        state['step'] += 1
        return 4, state  # ExamineBreathing

    if state['step'] == 4:
        state['step'] += 1
        return 5, state  # ExamineCirculation

    if state['step'] == 5:
        state['step'] += 1
        return 6, state  # ExamineDisability

    if state['step'] == 6:
        state['step'] += 1
        return 7, state  # ExamineExposure

    if state['step'] == 7:
        state['step'] += 1
        return 16, state  # ViewMonitor

    # Check vital signs
    if obs[39] == 0:
        return 25, state  # UseSatsProbe

    if obs[37] == 0:
        return 27, state  # UseBloodPressureCuff

    # Stabilize patient
    if obs[38] < 0.88:
        return 30, state  # UseNonRebreatherMask

    if obs[35] < 8:
        return 29, state  # UseBagValveMask

    if obs[37] < 60:
        return 15, state  # GiveFluids

    # Check for cardiac arrest
    if obs[38] < 0.65 or obs[37] < 20:
        return 17, state  # StartChestCompression

    # If patient is stable, finish
    if obs[38] >= 0.88 and obs[35] >= 8 and obs[37] >= 60:
        return 48, state  # Finish

    return 0, state  # DoNothing

state = {'step': 0}

for line in sys.stdin:
    action, state = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
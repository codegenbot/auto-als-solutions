import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if state['step'] == 0:
        state['step'] += 1
        return 1  # CheckSignsOfLife

    if state['step'] == 1:
        state['step'] += 1
        return 8  # ExamineResponse

    if state['step'] == 2:
        state['step'] += 1
        return 3  # ExamineAirway

    if state['step'] == 3:
        state['step'] += 1
        return 4  # ExamineBreathing

    if state['step'] == 4:
        state['step'] += 1
        return 5  # ExamineCirculation

    if state['step'] == 5:
        state['step'] += 1
        return 6  # ExamineDisability

    if state['step'] == 6:
        state['step'] += 1
        return 7  # ExamineExposure

    if state['step'] == 7:
        state['step'] += 1
        return 25  # UseSatsProbe

    if state['step'] == 8:
        state['step'] += 1
        return 27  # UseBloodPressureCuff

    if state['step'] == 9:
        state['step'] += 1
        return 16  # ViewMonitor

    # Check vital signs and intervene
    if obs[38] < 0.65 or obs[37] < 20:
        return 17  # StartChestCompression

    if obs[38] < 0.88:
        return 30  # UseNonRebreatherMask

    if obs[35] < 8:
        return 29  # UseBagValveMask

    if obs[37] < 60:
        return 15  # GiveFluids

    # If patient is stable, finish
    if obs[38] >= 0.88 and obs[35] >= 8 and obs[37] >= 60:
        return 48  # Finish

    # If we've done all checks and interventions, cycle through examinations
    state['step'] = 2  # Reset to ExamineAirway
    return 3  # ExamineAirway

state = {'step': 0}

for line in sys.stdin:
    action = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
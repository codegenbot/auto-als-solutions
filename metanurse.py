import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    # ABCDE Assessment
    if state['abcde'] < 5:
        if state['abcde'] == 0 and obs[7] == 0:
            state['abcde'] = 1
            return 8, state  # ExamineResponse
        if state['abcde'] == 1 and obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            state['abcde'] = 2
            return 3, state  # ExamineAirway
        if state['abcde'] == 2 and obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            state['abcde'] = 3
            return 4, state  # ExamineBreathing
        if state['abcde'] == 3 and obs[16] == 0 and obs[17] == 0:
            state['abcde'] = 4
            return 5, state  # ExamineCirculation
        if state['abcde'] == 4 and obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            state['abcde'] = 5
            return 6, state  # ExamineDisability
    
    # Critical conditions check
    if obs[7] > 0:  # BreathingNone detected
        if obs[18] == 0:
            return 18, state  # OpenAirwayDrawer
        return 29, state  # UseBagValveMask
    
    if obs[17] > 0:  # RadialPulseNonPalpable
        return 17, state  # StartChestCompression
    
    # Measure vital signs
    if obs[39] == 0:
        return 25, state  # UseSatsProbe
    if obs[37] == 0:
        return 38, state  # TakeBloodPressure
    if obs[40] == 0:
        return 26, state  # UseAline
    
    # Interventions based on vital signs
    if obs[39] > 0 and obs[46] < 0.88:
        return 30, state  # UseNonRebreatherMask
    if obs[40] > 0 and obs[47] < 8:
        if obs[18] == 0:
            return 18, state  # OpenAirwayDrawer
        return 29, state  # UseBagValveMask
    if obs[37] > 0 and obs[44] < 60:
        if obs[13] == 0:
            return 14, state  # UseVenflonIVCatheter
        return 15, state  # GiveFluids

    # Frequently measure vital signs
    if obs[39] < 0.9:
        return 25, state  # UseSatsProbe
    if obs[37] < 0.9:
        return 38, state  # TakeBloodPressure
    if obs[40] < 0.9:
        return 26, state  # UseAline

    # Check if patient is stabilized
    if (obs[39] > 0 and obs[46] >= 0.88 and
        obs[40] > 0 and obs[47] >= 8 and
        obs[37] > 0 and obs[44] >= 60):
        return 48, state  # Finish

    return 16, state  # ViewMonitor

state = {'abcde': 0}
for line in sys.stdin:
    action, state = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
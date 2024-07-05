import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state):
    if state['stage'] == 'A':
        if obs[0] == 0 and obs[1] == 0 and obs[2] == 0:
            return 8, 'A'  # ExamineResponse
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            return 3, 'A'  # ExamineAirway
        if obs[3] > 0 or obs[4] > 0 or obs[5] > 0 or obs[6] > 0:
            return 35, 'B'  # PerformAirwayManoeuvres, move to B
    elif state['stage'] == 'B':
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            return 4, 'B'  # ExamineBreathing
        if not state['sats_probe']:
            if not state['breathing_drawer']:
                return 19, 'B'  # OpenBreathingDrawer
            return 25, 'B'  # UseSatsProbe
        if obs[40] < 0.88 and not state['oxygen']:
            return 30, 'B'  # UseNonRebreatherMask
        return 16, 'C'  # ViewMonitor, move to C
    elif state['stage'] == 'C':
        if obs[16] == 0 and obs[17] == 0:
            return 5, 'C'  # ExamineCirculation
        if not state['bp_cuff']:
            return 27, 'C'  # UseBloodPressureCuff
        if obs[38] == 0:
            return 38, 'C'  # TakeBloodPressure
        return 16, 'D'  # ViewMonitor, move to D
    elif state['stage'] == 'D':
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            return 6, 'D'  # ExamineDisability
        return 16, 'E'  # ViewMonitor, move to E
    elif state['stage'] == 'E':
        if obs[25] == 0 and obs[26] == 0:
            return 7, 'E'  # ExamineExposure
        return 16, 'Monitor'  # ViewMonitor, move to monitoring
    else:  # Monitoring stage
        if obs[40] < 0.65 or obs[39] < 20:
            return 17, 'Monitor'  # StartChestCompression
        if obs[40] >= 0.88 and obs[41] >= 8 and obs[39] >= 60:
            return 48, 'Finish'  # Finish when stabilized
    return 16, state['stage']  # ViewMonitor as default action

state = {'stage': 'A', 'sats_probe': False, 'bp_cuff': False, 'breathing_drawer': False, 'oxygen': False}

for _ in range(350):
    observations = input()
    obs = parse_observations(observations)
    action, new_stage = choose_action(obs, state)
    state['stage'] = new_stage
    if action == 25:
        state['sats_probe'] = True
    elif action == 27:
        state['bp_cuff'] = True
    elif action == 19:
        state['breathing_drawer'] = True
    elif action == 30:
        state['oxygen'] = True
    print(action)
    sys.stdout.flush()
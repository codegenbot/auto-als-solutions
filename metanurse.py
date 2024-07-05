import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state):
    if state['phase'] == 'initial_setup':
        if obs[24] < 0.5:
            return 24, state  # UseMonitorPads
        if obs[25] < 0.5:
            return 25, state  # UseSatsProbe
        if obs[26] < 0.5:
            return 26, state  # UseAline
        if obs[27] < 0.5:
            return 27, state  # UseBloodPressureCuff
        state['phase'] = 'abcde_assessment'
        return 16, state  # ViewMonitor

    if state['phase'] == 'abcde_assessment':
        if obs[3] < 0.5:
            return 3, state  # ExamineAirway
        if obs[4] < 0.5:
            return 4, state  # ExamineBreathing
        if obs[5] < 0.5:
            return 5, state  # ExamineCirculation
        if obs[6] < 0.5:
            return 6, state  # ExamineDisability
        if obs[7] < 0.5:
            return 7, state  # ExamineExposure
        state['phase'] = 'treatment'
        return 16, state  # ViewMonitor

    if state['phase'] == 'treatment':
        if obs[46] > 0.5 and obs[-1] < 65:  # Sats < 65%
            return 17, state  # StartChestCompression
        if obs[45] > 0.5 and obs[-2] < 20:  # MAP < 20
            return 17, state  # StartChestCompression
        
        if obs[46] > 0.5 and obs[-1] < 88:  # Sats < 88%
            return 30, state  # UseNonRebreatherMask
        if obs[45] > 0.5 and obs[-2] < 60:  # MAP < 60
            return 15, state  # GiveFluids
        if obs[40] > 0.5 and obs[-7] < 8:  # RespRate < 8
            return 29, state  # UseBagValveMask
        if obs[38] > 0.5 and obs[-8] > 150:  # HeartRate > 150
            return 9, state  # GiveAdenosine

        if (obs[3] > 0.5 and  # AirwayClear
            obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
            obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
            obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
            return 48, state  # Finish

    return 16, state  # ViewMonitor (default action)

state = {'phase': 'initial_setup'}

for line in sys.stdin:
    observations = parse_observations(line)
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
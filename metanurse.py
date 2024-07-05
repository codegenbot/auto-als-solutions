import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state):
    state['step'] += 1
    
    if state['step'] > 300:
        return 48  # Finish if too many steps

    if obs[17] > 0.5:  # RadialPulseNonPalpable
        state['cpr_needed'] = True
        return 17  # StartChestCompression

    if state['cpr_needed']:
        if state['cpr_cycle'] < 30:
            state['cpr_cycle'] += 1
            return 17  # Continue chest compressions
        else:
            state['cpr_cycle'] = 0
            return 29  # BagDuringCPR

    if not state['monitor_on']:
        if obs[24] < 0.5:
            return 24  # UseMonitorPads
        elif obs[25] < 0.5:
            return 25  # UseSatsProbe
        elif obs[26] < 0.5:
            return 26  # UseAline
        elif obs[27] < 0.5:
            return 27  # UseBloodPressureCuff
        else:
            state['monitor_on'] = True
            return 16  # ViewMonitor

    if not state['abcde_complete']:
        if not state['airway']:
            state['airway'] = True
            return 3  # ExamineAirway
        elif not state['breathing']:
            state['breathing'] = True
            return 4  # ExamineBreathing
        elif not state['circulation']:
            state['circulation'] = True
            return 5  # ExamineCirculation
        elif not state['disability']:
            state['disability'] = True
            return 6  # ExamineDisability
        elif not state['exposure']:
            state['exposure'] = True
            return 7  # ExamineExposure
        else:
            state['abcde_complete'] = True

    if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
        return 30  # UseNonRebreatherMask

    if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
        return 15  # GiveFluids

    if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
        return 29  # UseBagValveMask

    if obs[38] > 0.5 and obs[-8] > 150 and obs[-1] >= 88 and obs[-2] >= 60 and obs[-7] >= 8:
        return 9  # GiveAdenosine only if other vitals are stable

    if (obs[3] > 0.5 and  # AirwayClear
        obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
        obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
        obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
        return 48  # Finish

    return 16  # ViewMonitor (default action to keep checking vitals)

state = {
    'step': 0,
    'cpr_needed': False,
    'cpr_cycle': 0,
    'monitor_on': False,
    'abcde_complete': False,
    'airway': False,
    'breathing': False,
    'circulation': False,
    'disability': False,
    'exposure': False
}

for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
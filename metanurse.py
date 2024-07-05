import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state):
    if state['step'] >= 350:
        return 48, state

    if state['phase'] == 'initial':
        if state['step'] == 0:
            state['phase'] = 'assess'
            return 1, state  # CheckSignsOfLife
    elif state['phase'] == 'assess':
        if not state['airway_checked']:
            state['airway_checked'] = True
            return 3, state  # ExamineAirway
        elif not state['breathing_checked']:
            state['breathing_checked'] = True
            return 4, state  # ExamineBreathing
        elif not state['circulation_checked']:
            state['circulation_checked'] = True
            return 5, state  # ExamineCirculation
        else:
            state['phase'] = 'equipment'
    elif state['phase'] == 'equipment':
        if not state['defibrillator_on']:
            state['defibrillator_on'] = True
            return 39, state  # TurnOnDefibrillator
        elif not state['monitor_pads']:
            state['monitor_pads'] = True
            return 24, state  # UseMonitorPads
        elif not state['sats_probe']:
            state['sats_probe'] = True
            return 25, state  # UseSatsProbe
        elif not state['venflonIV']:
            state['venflonIV'] = True
            return 14, state  # UseVenflonIVCatheter
        else:
            state['phase'] = 'treat'
    elif state['phase'] == 'treat':
        if obs[17] > 0.5:  # RadialPulseNonPalpable
            return 17, state  # StartChestCompression
        if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
            return 30, state  # UseNonRebreatherMask
        if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
            return 15, state  # GiveFluids
        if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
            return 29, state  # UseBagValveMask
        if (obs[3] > 0.5 and  # AirwayClear
            obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
            obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
            obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
            return 48, state  # Finish if stabilized

    return 16, state  # ViewMonitor (default action)

state = {
    'step': 0,
    'phase': 'initial',
    'airway_checked': False,
    'breathing_checked': False,
    'circulation_checked': False,
    'defibrillator_on': False,
    'monitor_pads': False,
    'sats_probe': False,
    'venflonIV': False
}

for line in sys.stdin:
    observations = parse_observations(line)
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
    state['step'] += 1
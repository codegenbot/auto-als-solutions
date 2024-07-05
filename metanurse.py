import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_count, state):
    if step_count >= 350:
        return 48, state  # Finish if step limit reached

    if 'signs_of_life_checked' not in state:
        state['signs_of_life_checked'] = True
        return 1, state  # CheckSignsOfLife

    if 'airway_examined' not in state:
        state['airway_examined'] = True
        return 3, state  # ExamineAirway

    if 'breathing_examined' not in state:
        state['breathing_examined'] = True
        return 4, state  # ExamineBreathing

    if 'circulation_examined' not in state:
        state['circulation_examined'] = True
        return 5, state  # ExamineCirculation

    if 'defibrillator_on' not in state:
        state['defibrillator_on'] = True
        return 39, state  # TurnOnDefibrillator

    if 'monitor_pads_used' not in state:
        state['monitor_pads_used'] = True
        return 24, state  # UseMonitorPads

    if 'sats_probe_used' not in state:
        state['sats_probe_used'] = True
        return 25, state  # UseSatsProbe

    if 'bp_cuff_used' not in state:
        state['bp_cuff_used'] = True
        return 27, state  # UseBloodPressureCuff

    if obs[17] > 0.5:  # RadialPulseNonPalpable
        return 17, state  # StartChestCompression

    if obs[7] > 0.5 or (obs[40] > 0.5 and obs[-7] < 8):  # BreathingNone or RespRate < 8
        return 29, state  # UseBagValveMask

    if 'oxygen_given' not in state:
        state['oxygen_given'] = True
        return 30, state  # UseNonRebreatherMask

    if 'iv_access' not in state:
        state['iv_access'] = True
        return 14, state  # UseVenflonIVCatheter

    if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
        return 15, state  # GiveFluids

    if (obs[3] > 0.5 and  # AirwayClear
        obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
        obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
        obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
        return 48, state  # Finish if stabilized

    return 16, state  # ViewMonitor (default action to keep checking vitals)

step_count = 0
state = {}
for line in sys.stdin:
    observations = parse_observations(line)
    action, state = choose_action(observations, step_count, state)
    print(action)
    sys.stdout.flush()
    step_count += 1
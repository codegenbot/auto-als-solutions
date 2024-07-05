import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_count, state):
    if step_count >= 350:
        return 48, state

    if state == 'initial':
        if step_count == 0:
            return 1, 'check_airway'  # CheckSignsOfLife
    elif state == 'check_airway':
        return 3, 'check_breathing'  # ExamineAirway
    elif state == 'check_breathing':
        return 4, 'check_circulation'  # ExamineBreathing
    elif state == 'check_circulation':
        return 5, 'setup_equipment'  # ExamineCirculation
    elif state == 'setup_equipment':
        if obs[39] < 0.5:  # TurnOnDefibrillator not done
            return 39, 'setup_equipment'
        elif obs[24] < 0.5:  # UseMonitorPads not used
            return 24, 'setup_equipment'
        elif obs[25] < 0.5:  # UseSatsProbe not used
            return 25, 'setup_equipment'
        elif obs[27] < 0.5:  # UseBloodPressureCuff not used
            return 27, 'setup_equipment'
        elif obs[14] < 0.5:  # UseVenflonIVCatheter not used
            return 14, 'treatment'
        else:
            return 16, 'treatment'  # ViewMonitor

    if state == 'treatment':
        if obs[17] > 0.5:  # RadialPulseNonPalpable
            return 17, 'cpr'  # StartChestCompression
        elif obs[7] > 0.5:  # BreathingNone
            return 29, 'treatment'  # UseBagValveMask
        elif obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
            return 30, 'treatment'  # UseNonRebreatherMask
        elif obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
            return 15, 'treatment'  # GiveFluids
        elif obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
            return 29, 'treatment'  # UseBagValveMask
        elif (obs[3] > 0.5 and  # AirwayClear
              obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
              obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
              obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
            return 48, 'finished'  # Finish if stabilized
        else:
            return 16, 'treatment'  # ViewMonitor

    if state == 'cpr':
        if step_count % 2 == 0:
            return 17, 'cpr'  # StartChestCompression
        else:
            return 10, 'cpr'  # GiveAdrenaline

    return 16, state  # ViewMonitor (default action)

state = 'initial'
step_count = 0
for line in sys.stdin:
    observations = parse_observations(line)
    action, state = choose_action(observations, step_count, state)
    print(action)
    sys.stdout.flush()
    step_count += 1
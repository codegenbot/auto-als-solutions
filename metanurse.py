import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_counter):
    if step_counter >= 350:
        return 48  # Finish if max steps reached

    if obs[17] > 0.5:  # RadialPulseNonPalpable
        return 17 if step_counter % 2 == 0 else 10  # Alternate between StartChestCompression and GiveAdrenaline

    if obs[7] > 0.5:  # BreathingNone
        return 29  # UseBagValveMask

    if obs[24] < 0.5:  # UseMonitorPads not used
        return 24

    if obs[16] < 0.5:  # ViewMonitor not recent
        return 16

    if obs[30] < 0.5:  # UseNonRebreatherMask not used
        return 30

    if obs[14] < 0.5:  # UseVenflonIVCatheter not used
        return 14

    if obs[15] < 0.5:  # GiveFluids not given
        return 15

    if obs[3] < 0.5:  # ExamineAirway not checked
        return 3
    if obs[4] < 0.5:  # ExamineBreathing not checked
        return 4
    if obs[5] < 0.5:  # ExamineCirculation not checked
        return 5
    if obs[6] < 0.5:  # ExamineDisability not checked
        return 6
    if obs[7] < 0.5:  # ExamineExposure not checked
        return 7

    if obs[25] < 0.5:  # UseSatsProbe not used
        return 25
    if obs[27] < 0.5:  # UseBloodPressureCuff not used
        return 27

    if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
        return 29  # UseBagValveMask

    if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
        return 15  # GiveFluids

    if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
        return 29  # UseBagValveMask

    if (obs[3] > 0.5 and  # AirwayClear
        obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
        obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
        obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
        return 48  # Finish if stabilized

    return 16  # ViewMonitor (default action to keep checking vitals)

step_counter = 0
for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations, step_counter)
    print(action)
    sys.stdout.flush()
    step_counter += 1
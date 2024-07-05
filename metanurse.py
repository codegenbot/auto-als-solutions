import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_count):
    if step_count >= 350:
        return 48  # Finish if step limit reached

    if obs[17] > 0.5:  # RadialPulseNonPalpable
        return 17 if step_count % 2 == 0 else 10  # Alternate between StartChestCompression and GiveAdrenaline

    if obs[7] > 0.5:  # BreathingNone
        return 29  # UseBagValveMask

    if obs[24] < 0.5:  # UseMonitorPads not used
        return 24  # UseMonitorPads

    if obs[25] < 0.5:  # UseSatsProbe not used
        return 25  # UseSatsProbe

    if obs[26] < 0.5:  # UseAline not used
        return 26  # UseAline

    if obs[39] < 0.5 or obs[40] < 0.5 or obs[41] < 0.5:
        return 16  # ViewMonitor

    if obs[3] < 0.5:  # AirwayClear not checked
        return 3  # ExamineAirway

    if obs[4] < 0.5:  # ExamineBreathing not done
        return 4  # ExamineBreathing

    if obs[30] < 0.5:  # UseNonRebreatherMask not used
        return 30  # UseNonRebreatherMask

    if obs[14] < 0.5:  # UseVenflonIVCatheter not used
        return 14  # UseVenflonIVCatheter

    if obs[15] < 0.5:  # GiveFluids not done
        return 15  # GiveFluids

    if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
        return 30  # UseNonRebreatherMask

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

step_count = 0
for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations, step_count)
    print(action)
    sys.stdout.flush()
    step_count += 1
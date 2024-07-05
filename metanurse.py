import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs):
    if obs[3] < 0.5:
        return 3  # ExamineAirway
    if obs[7] > 0.5:
        return 29  # UseBagValveMask
    if obs[11] < 0.5:
        return 4  # ExamineBreathing
    if obs[40] < 0.5:
        return 25  # UseSatsProbe
    if obs[46] > 0.5 and obs[-1] < 88:
        return 30  # UseNonRebreatherMask
    if obs[17] < 0.5:
        return 5  # ExamineCirculation
    if obs[39] < 0.5:
        return 27  # UseBloodPressureCuff
    if obs[45] > 0.5 and obs[-2] < 60:
        return 15  # GiveFluids
    if obs[21] < 0.5:
        return 6  # ExamineDisability
    if obs[27] < 0.5:
        return 7  # ExamineExposure
    if obs[46] > 0.5 and obs[-1] >= 88 and obs[45] > 0.5 and obs[-2] >= 60 and obs[40] > 0.5 and obs[-7] >= 8:
        return 48  # Finish
    return 16  # ViewMonitor

for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations)
    print(action)
    sys.stdout.flush()
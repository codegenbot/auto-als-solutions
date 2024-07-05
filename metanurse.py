import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs):
    if obs[7] > 0:  # BreathingNone
        return 29  # UseBagValveMask
    if obs[44] == 0:
        return 25  # UseSatsProbe
    if obs[45] == 0:
        return 27  # UseBloodPressureCuff
    if obs[46] > 0 and obs[52] < 88:
        return 30  # UseNonRebreatherMask
    if obs[45] > 0 and obs[51] < 60:
        return 15  # GiveFluids
    if obs[46] > 0 and obs[52] >= 88 and obs[45] > 0 and obs[51] >= 60 and obs[47] > 0 and obs[53] >= 8:
        return 48  # Finish
    return 16  # ViewMonitor

while True:
    observations = input()
    obs = parse_observations(observations)
    action = choose_action(obs)
    print(action)
    sys.stdout.flush()
    if action == 48:
        break
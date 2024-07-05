import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step):
    if step > 350:
        return 48  # Finish if timeout

    if obs[0] == 0 and obs[1] == 0 and obs[2] == 0:
        return 8  # ExamineResponse
    if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
        return 3  # ExamineAirway
    if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
        return 4  # ExamineBreathing
    if obs[46] == 0:
        return 25  # UseSatsProbe
    if obs[48] == 0:
        return 16  # ViewMonitor
    if obs[16] == 0 and obs[17] == 0:
        return 5  # ExamineCirculation
    if obs[45] == 0:
        return 27  # UseBloodPressureCuff
    if obs[48] == 0:
        return 16  # ViewMonitor
    if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
        return 6  # ExamineDisability
    if obs[25] == 0 and obs[26] == 0:
        return 7  # ExamineExposure

    if obs[7] > 0 and obs[46] > 0 and obs[52] == 0:
        return 29  # UseBagValveMask
    if obs[46] > 0 and obs[52] < 65:
        return 17  # StartChestCompression
    if obs[46] > 0 and obs[52] < 88:
        return 29  # UseBagValveMask
    if obs[46] > 0 and obs[52] >= 88 and obs[52] < 95:
        return 30  # UseNonRebreatherMask
    if obs[45] > 0 and obs[51] < 20:
        return 17  # StartChestCompression
    if obs[45] > 0 and obs[51] < 60:
        return 15  # GiveFluids
    if obs[47] > 0 and obs[49] < 8:
        return 29  # UseBagValveMask
    if obs[47] > 0 and obs[49] > 120:
        return 9  # GiveAdenosine

    if (obs[46] > 0 and obs[52] >= 88 and
        obs[45] > 0 and obs[51] >= 60 and
        obs[47] > 0 and obs[49] >= 8 and obs[49] <= 120):
        return 48  # Finish

    return 0  # DoNothing

step = 0
while True:
    observations = input()
    obs = parse_observations(observations)
    action = choose_action(obs, step)
    print(action)
    sys.stdout.flush()
    if action == 48:
        break
    step += 1
import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations):
    obs = parse_observations(observations)
    
    # Initial assessments
    if obs[7] == 0:
        return 8  # ExamineResponse
    if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
        return 3  # ExamineAirway
    if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
        return 4  # ExamineBreathing
    if obs[16] == 0 and obs[17] == 0:
        return 5  # ExamineCirculation
    if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
        return 6  # ExamineDisability
    if obs[25] == 0 and obs[26] == 0:
        return 7  # ExamineExposure

    # Vital signs measurements
    if obs[33] == 0:
        return 25  # UseSatsProbe
    if obs[34] == 0:
        return 27  # UseBloodPressureCuff
    if obs[35] == 0:
        return 16  # ViewMonitor

    # Check for critical conditions
    if obs[33] > 0 and obs[40] < 0.65:
        return 17  # StartChestCompression
    if obs[34] > 0 and obs[41] < 20:
        return 17  # StartChestCompression

    # Interventions
    if obs[33] > 0 and obs[40] < 0.88:
        return 30  # UseNonRebreatherMask
    if obs[35] > 0 and obs[42] < 8:
        return 29  # UseBagValveMask
    if obs[34] > 0 and obs[41] < 60:
        if obs[13] == 0:
            return 14  # UseVenflonIVCatheter
        return 15  # GiveFluids

    # Check if patient is stabilized
    if (obs[33] > 0 and obs[40] >= 0.88 and
        obs[35] > 0 and obs[42] >= 8 and
        obs[34] > 0 and obs[41] >= 60):
        return 48  # Finish

    return 0  # DoNothing

for line in sys.stdin:
    action = choose_action(line.strip())
    print(action)
    sys.stdout.flush()
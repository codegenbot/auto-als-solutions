import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs):
    if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:  # Check AVPU
        return 8  # ExamineResponse
    if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:  # Check Airway
        return 3  # ExamineAirway
    if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:  # Check Breathing
        return 4  # ExamineBreathing
    if obs[16] == 0 and obs[17] == 0:  # Check Circulation
        return 5  # ExamineCirculation
    if obs[23] == 0 and obs[24] == 0:  # Check Disability
        return 6  # ExamineDisability
    if obs[25] == 0 and obs[26] == 0:  # Check Exposure
        return 7  # ExamineExposure
    if obs[39] == 0:  # Check if MAP is measured
        return 27  # UseBloodPressureCuff
    if obs[40] == 0:  # Check if Sats is measured
        return 25  # UseSatsProbe
    if obs[46] < 88 and obs[40] > 0:  # If Sats < 88%
        return 30  # UseNonRebreatherMask
    if obs[45] < 60 and obs[39] > 0:  # If MAP < 60
        return 15  # GiveFluids
    return 48  # Finish

for step in range(350):
    observations = input()
    obs = parse_observations(observations)
    action = choose_action(obs)
    print(action)
    sys.stdout.flush()
    if action == 48:
        break
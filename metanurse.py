import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_counter):
    if step_counter >= 349:
        return 48  # Finish if approaching 350 steps
    
    if obs[0] == 0 and obs[1] == 0 and obs[2] == 0:
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
    
    if obs[44] == 0:
        return 25  # UseSatsProbe
    if obs[45] == 0:
        return 27  # UseBloodPressureCuff
    
    if obs[7] > 0:  # BreathingNone detected
        return 29  # UseBagValveMask
    
    if obs[46] > 0 and obs[52] < 88:
        return 30  # UseNonRebreatherMask
    if obs[45] > 0 and obs[51] < 60:
        return 15  # GiveFluids
    
    if obs[46] > 0 and obs[52] < 65 or (obs[45] > 0 and obs[51] < 20):
        return 17  # StartChestCompression
    
    if obs[28] == 0:
        return 2  # CheckRhythm
    
    if obs[46] > 0 and obs[52] >= 88 and obs[47] > 0 and obs[53] >= 8 and obs[45] > 0 and obs[51] >= 60:
        return 48  # Finish
    
    return 16  # ViewMonitor (regularly check vital signs)

step_counter = 0
while True:
    observations = input()
    obs = parse_observations(observations)
    action = choose_action(obs, step_counter)
    print(action)
    sys.stdout.flush()
    step_counter += 1
    if action == 48:
        break
import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(observations):
    obs = parse_observations(observations)
    
    # Check for critical conditions first
    if obs[38] < 0.65 or obs[45] < 20:  # Sats < 65% or MAP < 20mmHg
        return 17  # StartChestCompression
    
    # ABCDE assessment
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
    
    # Check vitals
    if obs[39] == 0:
        return 26  # UseSatsProbe
    
    if obs[41] == 0:
        return 27  # UseBloodPressureCuff
    
    if obs[38] < 0.88:
        return 30  # UseNonRebreatherMask
    
    if obs[40] < 8 or obs[45] < 60:
        return 15  # GiveFluids
    
    # If all checks pass, patient is stabilized
    return 48  # Finish

step = 0
while step < 350:
    observations = input().strip()
    action = choose_action(observations)
    print(action)
    sys.stdout.flush()
    
    if action == 48:  # Finish
        break
    
    step += 1
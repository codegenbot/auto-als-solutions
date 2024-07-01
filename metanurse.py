import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations):
    obs = parse_observations(observations)
    
    # Check for critical conditions first
    if obs[38] < 0.65 or obs[37] < 20:
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
    
    # Check vital signs
    if obs[37] == 0:
        return 38  # TakeBloodPressure
    
    if obs[38] == 0:
        return 25  # UseSatsProbe
    
    # Stabilize patient
    if obs[38] < 0.88:
        return 30  # UseNonRebreatherMask
    
    if obs[36] < 8:
        return 29  # UseBagValveMask
    
    if obs[37] < 60:
        return 15  # GiveFluids
    
    # If patient is stable, finish
    if obs[38] >= 0.88 and obs[36] >= 8 and obs[37] >= 60:
        return 48  # Finish
    
    return 0  # DoNothing

for line in sys.stdin:
    action = choose_action(line.strip())
    print(action)
    sys.stdout.flush()
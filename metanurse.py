import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    # ABCDE assessment sequence
    if state == 'A':
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            return 3, state  # ExamineAirway
        state = 'B'
    
    if state == 'B':
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            return 4, state  # ExamineBreathing
        if obs[39] == 0:
            return 25, state  # UseSatsProbe
        state = 'C'
    
    if state == 'C':
        if obs[16] == 0 and obs[17] == 0:
            return 5, state  # ExamineCirculation
        if obs[37] == 0:
            return 27, state  # UseBloodPressureCuff
        state = 'D'
    
    if state == 'D':
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            return 6, state  # ExamineDisability
        state = 'E'
    
    if state == 'E':
        if obs[25] == 0 and obs[26] == 0:
            return 7, state  # ExamineExposure
        state = 'Treatment'
    
    if state == 'Treatment':
        # Check vital signs
        if obs[46] == 0 or obs[47] == 0 or obs[48] == 0 or obs[49] == 0 or obs[50] == 0 or obs[51] == 0 or obs[52] == 0:
            return 16, state  # ViewMonitor
        
        # Cardiac arrest check
        if obs[51] < 0.65 or obs[50] < 20:
            return 17, state  # StartChestCompression
        
        # Stabilize patient
        if obs[51] < 0.88:
            return 30, state  # UseNonRebreatherMask
        
        if obs[52] < 8:
            return 29, state  # UseBagValveMask
        
        if obs[50] < 60:
            return 15, state  # GiveFluids
        
        # If patient is stable, finish
        if obs[51] >= 0.88 and obs[52] >= 8 and obs[50] >= 60:
            return 48, state  # Finish
    
    return 0, state  # DoNothing

state = 'A'
for line in sys.stdin:
    action, state = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
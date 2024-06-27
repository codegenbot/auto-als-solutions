import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, stage):
    obs = parse_observations(observations)
    
    # Attach monitoring equipment
    if stage == 0:
        return 25, 1  # UseSatsProbe
    elif stage == 1:
        return 27, 2  # UseBloodPressureCuff
    elif stage == 2:
        return 24, 3  # UseMonitorPads
    
    # ABCDE assessment
    elif stage == 3:
        return 8, 4  # ExamineResponse
    elif stage == 4:
        return 3, 5  # ExamineAirway
    elif stage == 5:
        return 4, 6  # ExamineBreathing
    elif stage == 6:
        return 5, 7  # ExamineCirculation
    elif stage == 7:
        return 6, 8  # ExamineDisability
    elif stage == 8:
        return 7, 9  # ExamineExposure
    
    # Check vital signs
    elif stage == 9:
        return 38, 10  # TakeBloodPressure
    elif stage == 10:
        return 16, 11  # ViewMonitor
    
    # Treat based on assessment
    elif stage >= 11:
        # Check for critical conditions
        if obs[38] < 0.65 or obs[39] < 20:
            return 17, stage  # StartChestCompression
        
        # Stabilize patient
        if obs[38] < 0.88:
            return 30, stage  # UseNonRebreatherMask
        
        if obs[35] < 8:
            return 29, stage  # UseBagValveMask
        
        if obs[39] < 60:
            return 15, stage  # GiveFluids
        
        # If patient is stable, finish
        if obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, stage  # Finish
    
    return 0, stage + 1  # DoNothing and progress to next stage

stage = 0
while True:
    observations = input().strip()
    if not observations:
        break
    action, stage = choose_action(observations, stage)
    print(action)
    sys.stdout.flush()
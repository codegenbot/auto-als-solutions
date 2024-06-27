import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, stage):
    obs = parse_observations(observations)
    
    # Attach monitoring equipment
    if stage == 0:
        if obs[24] == 0:
            return 25  # UseSatsProbe
        if obs[26] == 0:
            return 27  # UseBloodPressureCuff
        if obs[1] == 0:
            return 24  # UseMonitorPads
        stage = 1
    
    # ABCDE assessment
    if stage == 1:
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
        stage = 2
    
    # Check vital signs
    if stage == 2:
        if obs[39] == 0:
            return 38  # TakeBloodPressure
        if obs[38] == 0 or obs[35] == 0:
            return 16  # ViewMonitor
        stage = 3
    
    # Treat based on vital signs
    if stage == 3:
        if obs[38] < 0.65 or obs[39] < 20:
            return 17  # StartChestCompression
        if obs[38] < 0.88:
            return 30  # UseNonRebreatherMask
        if obs[35] < 8:
            return 29  # UseBagValveMask
        if obs[39] < 60:
            return 15  # GiveFluids
        stage = 4
    
    # Check if patient is stable
    if stage == 4:
        if obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48  # Finish
    
    return 0  # DoNothing

stage = 0
while True:
    observations = input().strip()
    if not observations:
        break
    action = choose_action(observations, stage)
    print(action)
    sys.stdout.flush()
    if action != 0:
        stage += 1
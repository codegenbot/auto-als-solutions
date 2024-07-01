import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations):
    obs = parse_observations(observations)
    
    # Immediate life-threatening conditions
    if obs[7] > 0:  # BreathingNone
        return 18 if obs[19] == 0 else 29  # OpenAirwayDrawer or UseBagValveMask
    
    # Check vital signs
    if obs[39] == 0:
        return 25  # UseSatsProbe
    if obs[37] == 0:
        return 27  # UseBloodPressureCuff
    
    # Critical conditions check
    if obs[39] > 0 and obs[37] > 0:
        if obs[46] < 0.65 or obs[44] < 20:
            return 17  # StartChestCompression
    
    # ABCDE assessment
    if obs[7] == 0 and obs[8] == 0:
        return 3  # ExamineAirway
    if obs[10] == 0:
        return 4  # ExamineBreathing
    if obs[16] == 0 and obs[17] == 0:
        return 5  # ExamineCirculation
    if obs[20] == 0 and obs[21] == 0:
        return 6  # ExamineDisability
    if obs[25] == 0:
        return 7  # ExamineExposure
    
    # Interventions
    if obs[46] < 0.88:
        return 30  # UseNonRebreatherMask
    if obs[47] < 8:
        return 29  # UseBagValveMask
    if obs[44] < 60:
        return 15 if obs[13] > 0 else 14  # GiveFluids or UseVenflonIVCatheter
    
    # Check if patient is stabilized
    if obs[46] >= 0.88 and obs[47] >= 8 and obs[44] >= 60:
        return 48  # Finish
    
    return 16  # ViewMonitor

for line in sys.stdin:
    action = choose_action(line.strip())
    print(action)
    sys.stdout.flush()
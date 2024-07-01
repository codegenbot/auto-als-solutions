import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations):
    obs = parse_observations(observations)
    
    # Check for cardiac arrest conditions
    if obs[46] < 0.65 or obs[44] < 20:
        return 17  # StartChestCompression

    # ABCDE assessment
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

    # Check and measure vital signs
    if obs[39] == 0:
        return 25  # UseSatsProbe
    if obs[37] == 0:
        return 27  # UseBloodPressureCuff
    if obs[40] == 0:
        return 38  # TakeBloodPressure

    # Handle breathing issues
    if obs[7] > 0:  # BreathingNone detected
        if obs[18] == 0:
            return 18  # OpenAirwayDrawer
        return 29  # UseBagValveMask

    # Interventions based on vital signs
    if obs[46] < 0.88:
        return 30  # UseNonRebreatherMask
    if obs[47] < 8:
        if obs[18] == 0:
            return 18  # OpenAirwayDrawer
        return 29  # UseBagValveMask
    if obs[44] < 60:
        if obs[13] == 0:
            return 14  # UseVenflonIVCatheter
        return 15  # GiveFluids

    # Check if patient is stabilized
    if obs[46] >= 0.88 and obs[47] >= 8 and obs[44] >= 60:
        return 48  # Finish

    return 16  # ViewMonitor

for line in sys.stdin:
    action = choose_action(line.strip())
    print(action)
    sys.stdout.flush()
import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations):
    obs = parse_observations(observations)
    
    # Start with basic assessments
    if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
        return 3  # ExamineAirway
    if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
        return 4  # ExamineBreathing
    if obs[16] == 0 and obs[17] == 0:
        return 5  # ExamineCirculation
    if obs[0] == 0 and obs[1] == 0 and obs[2] == 0:
        return 8  # ExamineResponse
    if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
        return 6  # ExamineDisability
    if obs[25] == 0 and obs[26] == 0:
        return 7  # ExamineExposure

    # Check and measure vital signs
    if obs[39] == 0:
        return 25  # UseSatsProbe
    if obs[37] == 0:
        return 38  # TakeBloodPressure
    if obs[33] == 0:
        return 26  # UseAline
    if obs[34] == 0:
        return 27  # UseBloodPressureCuff
    
    # Check if measurements are available
    sats_available = obs[39] > 0
    map_available = obs[37] > 0
    resp_available = obs[40] > 0
    
    # Critical conditions check
    if obs[7] > 0:  # BreathingNone detected
        return 18  # OpenAirwayDrawer
    
    if obs[7] > 0 and obs[18] > 0:  # BreathingNone and AirwayDrawer opened
        return 29  # UseBagValveMask
    
    if obs[17] > 0:  # RadialPulseNonPalpable
        return 17  # StartChestCompression
    
    # Interventions based on vital signs
    if sats_available and obs[46] < 0.88:
        return 30  # UseNonRebreatherMask
    
    if map_available and obs[44] < 60:
        if obs[13] == 0:
            return 14  # UseVenflonIVCatheter
        return 15  # GiveFluids
    
    # Check if patient is stabilized
    if (sats_available and obs[46] >= 0.88 and
        resp_available and obs[47] >= 8 and
        map_available and obs[44] >= 60 and
        obs[3] > 0):  # AirwayClear
        return 48  # Finish

    # Measure vital signs more frequently
    if obs[39] < 0.9:
        return 25  # UseSatsProbe
    if obs[37] < 0.9:
        return 38  # TakeBloodPressure
    if obs[40] < 0.9:
        return 16  # ViewMonitor

    return 0  # DoNothing

for line in sys.stdin:
    action = choose_action(line.strip())
    print(action)
    sys.stdout.flush()
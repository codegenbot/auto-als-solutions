import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations):
    obs = parse_observations(observations)
    
    if obs[7] > 0:  # BreathingNone
        return 18 if obs[18] == 0 else 29  # OpenAirwayDrawer or UseBagValveMask
    
    if obs[17] > 0:  # RadialPulseNonPalpable
        return 17  # StartChestCompression
    
    if obs[39] == 0:
        return 25  # UseSatsProbe
    if obs[37] == 0:
        return 38  # TakeBloodPressure
    
    sats_available = obs[39] > 0
    map_available = obs[37] > 0
    resp_available = obs[40] > 0
    
    if sats_available and obs[46] < 0.88:
        return 30  # UseNonRebreatherMask
    if resp_available and obs[47] < 8:
        return 29  # UseBagValveMask
    if map_available and obs[44] < 60:
        return 15  # GiveFluids
    
    if sats_available and obs[46] >= 0.88 and resp_available and obs[47] >= 8 and map_available and obs[44] >= 60:
        return 48  # Finish
    
    return 16  # ViewMonitor

for line in sys.stdin:
    action = choose_action(line.strip())
    print(action)
    sys.stdout.flush()
import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, step_count):
    obs = parse_observations(observations)
    
    if step_count > 350:
        return 48  # Finish due to timeout

    if obs[39] == 0:
        return 25  # UseSatsProbe
    if obs[37] == 0:
        return 27  # UseBloodPressureCuff

    sats_available = obs[39] > 0
    map_available = obs[37] > 0
    resp_available = obs[40] > 0

    if sats_available and map_available:
        if obs[46] < 0.65 or obs[44] < 20:
            return 17  # StartChestCompression

    if obs[7] > 0:  # BreathingNone detected
        if obs[18] == 0:
            return 18  # OpenAirwayDrawer
        return 29  # UseBagValveMask

    if sats_available and obs[46] < 0.88:
        return 30  # UseNonRebreatherMask
    if resp_available and obs[47] < 8:
        if obs[18] == 0:
            return 18  # OpenAirwayDrawer
        return 29  # UseBagValveMask
    if map_available and obs[44] < 60:
        if obs[13] == 0:
            return 14  # UseVenflonIVCatheter
        return 15  # GiveFluids

    if (sats_available and obs[46] >= 0.88 and
        resp_available and obs[47] >= 8 and
        map_available and obs[44] >= 60):
        return 48  # Finish

    return 16  # ViewMonitor

step_count = 0
for line in sys.stdin:
    step_count += 1
    action = choose_action(line.strip(), step_count)
    print(action)
    sys.stdout.flush()
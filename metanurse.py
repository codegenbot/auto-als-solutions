import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, action_counter):
    obs = parse_observations(observations)
    
    # Initial assessments
    if obs[7] == 0:
        return 8, action_counter  # ExamineResponse
    if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
        return 3, action_counter  # ExamineAirway
    
    # Open airway drawer and use bag valve mask if no breathing
    if obs[7] > 0 and obs[8] == 0:
        if action_counter['OpenAirwayDrawer'] == 0:
            action_counter['OpenAirwayDrawer'] += 1
            return 18, action_counter  # OpenAirwayDrawer
        elif action_counter['UseBagValveMask'] == 0:
            action_counter['UseBagValveMask'] += 1
            return 29, action_counter  # UseBagValveMask
    
    # Check signs of life and start chest compressions if no breathing
    if obs[7] > 0 and obs[8] == 0:
        if action_counter['CheckSignsOfLife'] == 0:
            action_counter['CheckSignsOfLife'] += 1
            return 1, action_counter  # CheckSignsOfLife
        elif action_counter['StartChestCompression'] == 0:
            action_counter['StartChestCompression'] += 1
            return 17, action_counter  # StartChestCompression
    
    # Vital signs monitoring
    if obs[33] == 0:
        return 25, action_counter  # UseSatsProbe
    if obs[34] == 0:
        return 27, action_counter  # UseBloodPressureCuff
    if obs[35] == 0:
        return 16, action_counter  # ViewMonitor
    
    # Examine breathing and circulation
    if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
        return 4, action_counter  # ExamineBreathing
    if obs[16] == 0 and obs[17] == 0:
        return 5, action_counter  # ExamineCirculation
    
    # Examine disability and exposure
    if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
        return 6, action_counter  # ExamineDisability
    if obs[25] == 0 and obs[26] == 0:
        return 7, action_counter  # ExamineExposure

    # Interventions based on vital signs
    if obs[33] > 0 and obs[40] < 0.88:
        return 30, action_counter  # UseNonRebreatherMask
    if obs[35] > 0 and obs[42] < 8:
        return 29, action_counter  # UseBagValveMask
    if obs[34] > 0 and obs[41] < 60:
        if obs[13] == 0:
            return 14, action_counter  # UseVenflonIVCatheter
        return 15, action_counter  # GiveFluids

    # Check if patient is stabilized
    if (obs[33] > 0 and obs[40] >= 0.88 and
        obs[35] > 0 and obs[42] >= 8 and
        obs[34] > 0 and obs[41] >= 60):
        return 48, action_counter  # Finish

    return 0, action_counter  # DoNothing

action_counter = {
    'OpenAirwayDrawer': 0,
    'UseBagValveMask': 0,
    'CheckSignsOfLife': 0,
    'StartChestCompression': 0
}

step_count = 0
for line in sys.
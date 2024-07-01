import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state, action_counts, equipment_status):
    if action_counts[state] > 5:
        state = (state + 1) % 5

    if obs[45] < 20 or obs[46] < 65:
        return 17, state  # StartChestCompression

    if state == 0:  # Airway
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            action_counts[0] += 1
            return 8, state  # ExamineResponse
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            action_counts[0] += 1
            return 3, state  # ExamineAirway
        else:
            state = 1
    
    if state == 1:  # Breathing
        if not equipment_status['breathing_drawer']:
            equipment_status['breathing_drawer'] = True
            return 19, state  # OpenBreathingDrawer
        if not equipment_status['non_rebreather']:
            equipment_status['non_rebreather'] = True
            return 30, state  # UseNonRebreatherMask
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            action_counts[1] += 1
            return 4, state  # ExamineBreathing
        else:
            state = 2

    if state == 2:  # Circulation
        if not equipment_status['circulation_drawer']:
            equipment_status['circulation_drawer'] = True
            return 20, state  # OpenCirculationDrawer
        if not equipment_status['bp_cuff']:
            equipment_status['bp_cuff'] = True
            return 27, state  # UseBloodPressureCuff
        if not equipment_status['sats_probe']:
            equipment_status['sats_probe'] = True
            return 25, state  # UseSatsProbe
        if not equipment_status['venflon']:
            equipment_status['venflon'] = True
            return 14, state  # UseVenflonIVCatheter
        if obs[16] == 0 and obs[17] == 0:
            action_counts[2] += 1
            return 5, state  # ExamineCirculation
        else:
            state = 3

    if state == 3:  # Disability
        if obs[23] == 0 and obs[24] == 0:
            action_counts[3] += 1
            return 6, state  # ExamineDisability
        else:
            state = 4

    if state == 4:  # Exposure
        if obs[25] == 0 and obs[26] == 0:
            action_counts[4] += 1
            return 7, state  # ExamineExposure
        else:
            state = 0

    if obs[46] < 88 and equipment_status['non_rebreather']:
        return 30, state  # UseNonRebreatherMask
    if obs[45] < 60 and equipment_status['venflon']:
        return 15, state  # GiveFluids
    
    if not equipment_status['monitor_viewed']:
        equipment_status['monitor_viewed'] = True
        return 16, state  # ViewMonitor

    if obs[46] >= 88 and obs[45] >= 60 and obs[41] >= 8:
        return 48, state  # Finish

    return 0, state  # DoNothing

state = 0
action_counts = [0, 0, 0, 0, 0]
equipment_status = {
    'breathing_drawer': False,
    'circulation_drawer': False,
    'bp_cuff': False,
    'sats_probe': False,
    'venflon': False,
    '
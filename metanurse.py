import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state, action_counts, equipment_state):
    if action_counts[state] > 5:
        state = (state + 1) % 5

    if obs[45] < 20 or obs[46] < 65:
        return 17, state  # StartChestCompression

    if not equipment_state['monitor']:
        return 16, state  # ViewMonitor

    if not equipment_state['bp_cuff']:
        return 27, state  # UseBloodPressureCuff

    if not equipment_state['sats_probe']:
        return 25, state  # UseSatsProbe

    if not equipment_state['circulation_drawer']:
        return 20, state  # OpenCirculationDrawer

    if not equipment_state['iv_catheter']:
        return 14, state  # UseVenflonIVCatheter

    if not equipment_state['breathing_drawer']:
        return 19, state  # OpenBreathingDrawer

    if not equipment_state['oxygen_mask'] and obs[46] < 88:
        return 30, state  # UseNonRebreatherMask

    if state == 0:  # Airway
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            action_counts[0] += 1
            return 8, state  # ExamineResponse
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            action_counts[0] += 1
            return 3, state  # ExamineAirway
        state = 1

    if state == 1:  # Breathing
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            action_counts[1] += 1
            return 4, state  # ExamineBreathing
        if obs[41] < 8:
            action_counts[1] += 1
            return 29, state  # UseBagValveMask
        state = 2

    if state == 2:  # Circulation
        if obs[16] == 0 and obs[17] == 0:
            action_counts[2] += 1
            return 5, state  # ExamineCirculation
        if obs[45] < 60:
            action_counts[2] += 1
            return 15, state  # GiveFluids
        state = 3

    if state == 3:  # Disability
        if obs[23] == 0 and obs[24] == 0:
            action_counts[3] += 1
            return 6, state  # ExamineDisability
        state = 4

    if state == 4:  # Exposure
        if obs[25] == 0 and obs[26] == 0:
            action_counts[4] += 1
            return 7, state  # ExamineExposure
        state = 0

    if obs[46] >= 88 and obs[45] >= 60 and obs[41] >= 8:
        return 48, state  # Finish

    return 0, state  # DoNothing

state = 0
action_counts = [0, 0, 0, 0, 0]
equipment_state = {
    'monitor': False,
    'bp_cuff': False,
    'sats_probe': False,
    'circulation_drawer': False,
    'iv_catheter': False,
    'breathing_drawer': False,
    'oxygen_mask': False
}

for step in range(350):
    observations = input()
    obs = parse_observations(observations)
    action, state = choose_action(obs, state, action_counts, equipment_state)

    if action == 16:
        equipment_state['monitor'] = True
    elif action == 27:
        equipment_state['bp_cuff'] = True
    elif action ==
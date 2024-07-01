import sys
import time

def parse_observations(observations):
    return list(map(float, observations.split()))

class State:
    def __init__(self):
        self.last_action_time = {}
        self.step = 'A'
        self.airway_clear = False
        self.breathing_normal = False
        self.circulation_normal = False
        self.disability_normal = False
        self.exposure_normal = False

def action_cooldown(state, action, cooldown=5):
    current_time = time.time()
    if action in state.last_action_time and current_time - state.last_action_time[action] < cooldown:
        return False
    state.last_action_time[action] = current_time
    return True

def choose_action(obs, state):
    if state.step == 'A':
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0 and action_cooldown(state, 8):
            return 8  # ExamineResponse
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0 and action_cooldown(state, 3):
            return 3  # ExamineAirway
        if obs[3] > 0:
            state.airway_clear = True
            state.step = 'B'
    
    if state.step == 'B':
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0 and action_cooldown(state, 4):
            return 4  # ExamineBreathing
        if obs[7] > 0:  # BreathingNone
            if action_cooldown(state, 17):
                return 17  # StartChestCompression
            if action_cooldown(state, 29):
                return 29  # UseBagValveMask
        if obs[10] > 0:  # BreathingEqualChestExpansion
            state.breathing_normal = True
            state.step = 'C'
    
    if state.step == 'C':
        if obs[16] == 0 and obs[17] == 0 and action_cooldown(state, 5):
            return 5  # ExamineCirculation
        if obs[39] == 0 and action_cooldown(state, 27):
            return 27  # UseBloodPressureCuff
        if obs[40] == 0 and action_cooldown(state, 25):
            return 25  # UseSatsProbe
        if obs[46] < 88 and obs[40] > 0 and action_cooldown(state, 30):
            return 30  # UseNonRebreatherMask
        if obs[45] < 60 and obs[39] > 0 and action_cooldown(state, 15):
            return 15  # GiveFluids
        if obs[16] > 0 and obs[45] >= 60 and obs[46] >= 88:
            state.circulation_normal = True
            state.step = 'D'
    
    if state.step == 'D':
        if obs[23] == 0 and obs[24] == 0 and action_cooldown(state, 6):
            return 6  # ExamineDisability
        if (obs[20] > 0 or obs[21] > 0 or obs[22] > 0) and obs[24] > 0:
            state.disability_normal = True
            state.step = 'E'
    
    if state.step == 'E':
        if obs[25] == 0 and obs[26] == 0 and action_cooldown(state, 7):
            return 7  # ExamineExposure
        if obs[25] > 0 or obs[26] > 0:
            state.exposure_normal = True
    
    if state.airway_clear and state.breathing_normal and state.
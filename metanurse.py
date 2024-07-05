import sys
import time

def parse_observations(observations):
    return list(map(float, observations.split()))

class ResuscitationState:
    INITIAL = 0
    AIRWAY = 1
    BREATHING = 2
    CIRCULATION = 3
    DISABILITY = 4
    EXPOSURE = 5
    REASSESS = 6
    CPR = 7

def choose_action(obs, state, last_action_time):
    current_time = time.time()
    
    if current_time - last_action_time < 0.5:
        return 0, state, last_action_time

    if state == ResuscitationState.INITIAL:
        return 1, ResuscitationState.AIRWAY, current_time

    if state == ResuscitationState.AIRWAY:
        if obs[3] < 0.5:
            return 3, state, current_time
        if obs[7] > 0.5:  # BreathingNone
            return 18, ResuscitationState.BREATHING, current_time  # OpenAirwayDrawer
        return 29, ResuscitationState.BREATHING, current_time

    if state == ResuscitationState.BREATHING:
        if obs[7] > 0.5:  # BreathingNone
            return 29, ResuscitationState.CPR, current_time  # UseBagValveMask
        if obs[11] < 0.5:
            return 4, state, current_time
        if obs[40] < 0.5:
            return 25, state, current_time  # UseSatsProbe
        if obs[46] > 0.5 and obs[-1] < 88:
            return 30, state, current_time
        return 27, ResuscitationState.CIRCULATION, current_time

    if state == ResuscitationState.CIRCULATION:
        if obs[17] < 0.5:
            return 5, state, current_time
        if obs[39] < 0.5:
            return 27, state, current_time  # UseBloodPressureCuff
        if obs[45] > 0.5 and obs[-2] < 60:
            return 15, state, current_time  # GiveFluids
        return 6, ResuscitationState.DISABILITY, current_time

    if state == ResuscitationState.DISABILITY:
        if obs[21] < 0.5:
            return 6, state, current_time
        return 7, ResuscitationState.EXPOSURE, current_time

    if state == ResuscitationState.EXPOSURE:
        if obs[27] < 0.5:
            return 7, state, current_time
        return 16, ResuscitationState.REASSESS, current_time  # ViewMonitor

    if state == ResuscitationState.REASSESS:
        if obs[46] > 0.5 and obs[-1] >= 88 and obs[45] > 0.5 and obs[-2] >= 60 and obs[40] > 0.5 and obs[-7] >= 8:
            return 48, state, current_time  # Finish
        return 2, ResuscitationState.AIRWAY, current_time  # CheckRhythm

    if state == ResuscitationState.CPR:
        if obs[17] > 0.5:
            return 3, ResuscitationState.AIRWAY, current_time
        if current_time - last_action_time > 60:
            return 10, state, current_time  # GiveAdrenaline
        if obs[28] < 0.5:
            return 28, state, current_time  # AttachDefibPads
        if obs[39] < 0.5:
            return 39, state, current_time  # TurnOnDefibrillator
        return 17, state, current_time  # StartChestCompression

    return 0, state, current_time

state = ResuscitationState.INITIAL
last_action_time = time.time() - 10
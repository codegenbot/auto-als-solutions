import sys

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

def is_stable(obs):
    return (obs[46] > 0.5 and obs[-1] >= 88 and
            obs[45] > 0.5 and obs[-2] >= 60 and
            obs[40] > 0.5 and obs[-7] >= 8)

def choose_action(obs, state, step_count):
    if step_count > 350:
        return 48, state, step_count + 1

    if state == ResuscitationState.INITIAL:
        return 8, ResuscitationState.AIRWAY, step_count + 1

    if state == ResuscitationState.AIRWAY:
        if obs[3] < 0.5:
            return 3, state, step_count + 1
        if obs[7] > 0.5:
            return 35, state, step_count + 1
        if is_stable(obs):
            return 16, ResuscitationState.REASSESS, step_count + 1
        return 18, ResuscitationState.BREATHING, step_count + 1

    if state == ResuscitationState.BREATHING:
        if obs[7] > 0.5:
            return 1, ResuscitationState.CPR, step_count + 1
        if obs[11] < 0.5:
            return 4, state, step_count + 1
        if obs[40] < 0.5:
            return 25, state, step_count + 1
        if obs[46] > 0.5 and obs[-1] < 88:
            return 30, state, step_count + 1
        if is_stable(obs):
            return 16, ResuscitationState.REASSESS, step_count + 1
        return 19, ResuscitationState.CIRCULATION, step_count + 1

    if state == ResuscitationState.CIRCULATION:
        if obs[17] < 0.5:
            return 5, state, step_count + 1
        if obs[39] < 0.5:
            return 27, state, step_count + 1
        if obs[45] > 0.5 and obs[-2] < 60:
            return 15, state, step_count + 1
        if is_stable(obs):
            return 16, ResuscitationState.REASSESS, step_count + 1
        return 20, ResuscitationState.DISABILITY, step_count + 1

    if state == ResuscitationState.DISABILITY:
        if obs[21] < 0.5:
            return 6, state, step_count + 1
        if is_stable(obs):
            return 16, ResuscitationState.REASSESS, step_count + 1
        return 7, ResuscitationState.EXPOSURE, step_count + 1

    if state == ResuscitationState.EXPOSURE:
        if obs[27] < 0.5:
            return 7, state, step_count + 1
        if is_stable(obs):
            return 16, ResuscitationState.REASSESS, step_count + 1
        return 16, ResuscitationState.REASSESS, step_count + 1

    if state == ResuscitationState.REASSESS:
        if is_stable(obs):
            return 48, state, step_count + 1
        return 3, ResuscitationState.AIRWAY, step_count + 1

    if state == ResuscitationState.CPR:
        if obs[7] < 0.5 and obs[17] > 0.5:
            return 3, ResuscitationState.AIRWAY, step_count + 1
        if obs[28] < 0.5
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

def choose_action(obs, state):
    if state == ResuscitationState.INITIAL:
        return 1, ResuscitationState.AIRWAY

    if state == ResuscitationState.AIRWAY:
        if obs[3] < 0.5:
            return 3, state
        if obs[7] > 0.5:
            return 29, state
        return 18, ResuscitationState.BREATHING

    if state == ResuscitationState.BREATHING:
        if obs[7] > 0.5:
            return 1, ResuscitationState.CPR
        if obs[11] < 0.5:
            return 4, state
        if obs[40] < 0.5:
            return 25, state
        if obs[39] < 0.5:
            return 27, state
        if obs[46] > 0.5 and obs[-1] < 88:
            return 30, state
        return 19, ResuscitationState.CIRCULATION

    if state == ResuscitationState.CIRCULATION:
        if obs[17] < 0.5:
            return 5, state
        if obs[39] < 0.5:
            return 38, state
        if obs[45] > 0.5 and obs[-2] < 60:
            return 15, state
        return 20, ResuscitationState.DISABILITY

    if state == ResuscitationState.DISABILITY:
        if obs[21] < 0.5:
            return 6, state
        return 21, ResuscitationState.EXPOSURE

    if state == ResuscitationState.EXPOSURE:
        if obs[27] < 0.5:
            return 7, state
        return 16, ResuscitationState.REASSESS

    if state == ResuscitationState.REASSESS:
        if obs[46] > 0.5 and obs[-1] >= 88 and obs[45] > 0.5 and obs[-2] >= 60 and obs[40] > 0.5 and obs[-7] >= 8:
            return 48, state
        return 3, ResuscitationState.AIRWAY

    if state == ResuscitationState.CPR:
        if obs[17] > 0.5:
            return 3, ResuscitationState.AIRWAY
        if obs[28] < 0.5:
            return 28, state
        if obs[39] < 0.5:
            return 39, state
        return 17, state

    return 0, state

state = ResuscitationState.INITIAL

for line in sys.stdin:
    try:
        observations = parse_observations(line)
        action, state = choose_action(observations, state)
        print(action)
        sys.stdout.flush()
    except Exception:
        print(0)
        sys.stdout.flush()
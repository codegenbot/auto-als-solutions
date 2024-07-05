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

def choose_action(obs, state):
    if state == ResuscitationState.INITIAL:
        return 25, ResuscitationState.AIRWAY  # Attach sats probe first

    if state == ResuscitationState.AIRWAY:
        if obs[3] < 0.5:
            return 3, state  # Examine airway
        if obs[7] > 0.5:
            return 35, state  # Perform airway maneuvers
        return 29, ResuscitationState.BREATHING  # Use bag valve mask

    if state == ResuscitationState.BREATHING:
        if obs[40] < 0.5:
            return 4, state  # Examine breathing
        if obs[46] > 0.5 and obs[-1] < 88:
            return 30, state  # Use non-rebreather mask
        return 27, ResuscitationState.CIRCULATION  # Use blood pressure cuff

    if state == ResuscitationState.CIRCULATION:
        if obs[39] < 0.5:
            return 38, state  # Take blood pressure
        if obs[45] > 0.5 and obs[-2] < 60:
            return 15, state  # Give fluids
        return 6, ResuscitationState.DISABILITY  # Examine disability

    if state == ResuscitationState.DISABILITY:
        if obs[21] < 0.5:
            return 6, state  # Examine disability
        return 7, ResuscitationState.EXPOSURE  # Examine exposure

    if state == ResuscitationState.EXPOSURE:
        if obs[27] < 0.5:
            return 7, state  # Examine exposure
        return 16, ResuscitationState.REASSESS  # View monitor

    if state == ResuscitationState.REASSESS:
        if obs[46] > 0.5 and obs[-1] >= 88 and obs[45] > 0.5 and obs[-2] >= 60 and obs[40] > 0.5 and obs[-7] >= 8:
            return 48, state  # Finish if stabilized
        return 3, ResuscitationState.AIRWAY  # Start ABCDE assessment again

    return 0, state  # Default action

state = ResuscitationState.INITIAL

for line in sys.stdin:
    try:
        observations = parse_observations(line)
        action, state = choose_action(observations, state)
        print(action)
        sys.stdout.flush()
    except Exception:
        print(0)  # Default to DoNothing if unexpected error occurs
        sys.stdout.flush()
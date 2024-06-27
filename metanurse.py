import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

class State:
    INITIAL = 0
    AIRWAY = 1
    BREATHING = 2
    CIRCULATION = 3
    DISABILITY = 4
    EXPOSURE = 5
    STABILIZING = 6

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if state == State.INITIAL:
        return 8, State.AIRWAY  # ExamineResponse
    
    elif state == State.AIRWAY:
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            return 3, State.AIRWAY  # ExamineAirway
        else:
            return 29, State.BREATHING  # UseBagValveMask
    
    elif state == State.BREATHING:
        if obs[39] == 0:
            return 25, State.BREATHING  # UseSatsProbe
        elif obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            return 4, State.BREATHING  # ExamineBreathing
        else:
            return 30, State.CIRCULATION  # UseNonRebreatherMask
    
    elif state == State.CIRCULATION:
        if obs[41] == 0:
            return 27, State.CIRCULATION  # UseBloodPressureCuff
        elif obs[16] == 0 and obs[17] == 0:
            return 5, State.CIRCULATION  # ExamineCirculation
        else:
            return 14, State.DISABILITY  # UseVenflonIVCatheter
    
    elif state == State.DISABILITY:
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            return 6, State.DISABILITY  # ExamineDisability
        else:
            return 33, State.EXPOSURE  # TakeBloodForArtherialBloodGas
    
    elif state == State.EXPOSURE:
        if obs[25] == 0 and obs[26] == 0:
            return 7, State.EXPOSURE  # ExamineExposure
        else:
            return 16, State.STABILIZING  # ViewMonitor
    
    elif state == State.STABILIZING:
        if obs[39] > 0 and obs[46] < 0.88:
            return 30, State.STABILIZING  # UseNonRebreatherMask
        elif obs[41] > 0 and obs[45] < 60:
            return 15, State.STABILIZING  # GiveFluids
        elif obs[40] > 0 and obs[46] < 8:
            return 29, State.STABILIZING  # UseBagValveMask
        elif obs[39] > 0 and obs[46] >= 0.88 and obs[41] > 0 and obs[45] >= 60 and obs[40] > 0 and obs[46] >= 8:
            return 48, State.INITIAL  # Finish
        else:
            return 16, State.STABILIZING  # ViewMonitor
    
    return 0, state  # DoNothing

state = State.INITIAL
step = 0
while step < 350:
    observations = input().strip()
    action, new_state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
    
    if action == 48:  # Finish
        break
    
    state = new_state
    step += 1
import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if state == 'start':
        return 8, 'response'  # ExamineResponse
    elif state == 'response':
        return 3, 'airway'  # ExamineAirway
    elif state == 'airway':
        return 4, 'breathing'  # ExamineBreathing
    elif state == 'breathing':
        return 5, 'circulation'  # ExamineCirculation
    elif state == 'circulation':
        return 6, 'disability'  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure'  # ExamineExposure
    elif state == 'exposure':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        if obs[38] == 0:
            return 25, 'monitor'  # UseSatsProbe
        elif obs[39] == 0:
            return 27, 'monitor'  # UseBloodPressureCuff
        elif obs[34] == 0:
            return 38, 'monitor'  # TakeBloodPressure
        else:
            return 0, 'assess'  # DoNothing, move to assessment
    elif state == 'assess':
        if obs[38] < 0.65 or obs[39] < 20:
            return 17, 'cpr'  # StartChestCompression
        elif obs[3] == 0:
            return 35, 'assess'  # PerformAirwayManoeuvres
        elif obs[38] < 0.88:
            return 30, 'assess'  # UseNonRebreatherMask
        elif obs[35] < 8:
            return 29, 'assess'  # UseBagValveMask
        elif obs[39] < 60:
            return 15, 'assess'  # GiveFluids
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'monitor'  # ViewMonitor
    elif state == 'cpr':
        if obs[38] >= 0.65 and obs[39] >= 20:
            return 0, 'assess'  # DoNothing, return to assessment
        else:
            return 17, 'cpr'  # Continue CPR
    
    return 0, state  # DoNothing if no other action is appropriate

state = 'start'
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
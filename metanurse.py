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
        return 25, 'attach_sats'  # UseSatsProbe
    elif state == 'attach_sats':
        return 27, 'attach_bp'  # UseBloodPressureCuff
    elif state == 'attach_bp':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        sats = obs[-2] if obs[-8] > 0 else 0
        map = obs[-3] if obs[-9] > 0 else 0
        resp_rate = obs[-1] if obs[-7] > 0 else 0
        heart_rate = obs[-7] if obs[-13] > 0 else 0

        if sats < 0.65 or map < 20:
            return 17, 'cpr'  # StartChestCompression
        elif sats < 0.88:
            return 30, 'oxygen'  # UseNonRebreatherMask
        elif resp_rate < 8:
            return 29, 'ventilation'  # UseBagValveMask
        elif map < 60:
            return 15, 'fluids'  # GiveFluids
        elif heart_rate > 100:
            return 9, 'adenosine'  # GiveAdenosine
        elif sats >= 0.88 and resp_rate >= 8 and map >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'monitor'  # ViewMonitor again
    elif state in ['oxygen', 'ventilation', 'fluids', 'adenosine', 'cpr']:
        return 16, 'monitor'  # ViewMonitor after treatment
    else:
        return 16, 'monitor'  # Default to viewing monitor

state = 'start'
for line in sys.stdin:
    action, new_state = choose_action(line.strip(), state)
    print(action)
    sys.stdout.flush()
    state = new_state
    if state == 'finish':
        break
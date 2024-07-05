import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def is_stabilized(obs):
    return obs[39] > 0 and obs[46] >= 88 and obs[41] >= 8 and obs[44] >= 60

def choose_action(obs, state):
    if state == 'start':
        return 8, 'response'  # ExamineResponse
    elif state == 'response':
        if obs[0] > 0 or obs[1] > 0:
            return 3, 'airway'  # ExamineAirway
        else:
            return 17, 'cpr'  # StartChestCompression
    elif state == 'airway':
        if obs[3] > 0:
            return 4, 'breathing'  # ExamineBreathing
        else:
            return 35, 'airway_maneuvers'  # PerformAirwayManoeuvres
    elif state == 'airway_maneuvers':
        return 4, 'breathing'  # ExamineBreathing
    elif state == 'breathing':
        if obs[10] == 0:
            return 19, 'open_breathing_drawer'  # OpenBreathingDrawer
        elif obs[34] == 0:
            return 25, 'use_sats_probe'  # UseSatsProbe
        else:
            return 5, 'circulation'  # ExamineCirculation
    elif state == 'open_breathing_drawer':
        return 25, 'use_sats_probe'  # UseSatsProbe
    elif state == 'use_sats_probe':
        if obs[46] < 88:
            return 30, 'use_mask'  # UseNonRebreatherMask
        else:
            return 5, 'circulation'  # ExamineCirculation
    elif state == 'use_mask':
        return 5, 'circulation'  # ExamineCirculation
    elif state == 'circulation':
        if obs[35] == 0:
            return 27, 'use_bp_cuff'  # UseBloodPressureCuff
        elif obs[38] == 0:
            return 38, 'take_bp'  # TakeBloodPressure
        else:
            return 6, 'disability'  # ExamineDisability
    elif state == 'use_bp_cuff':
        return 38, 'take_bp'  # TakeBloodPressure
    elif state == 'take_bp':
        if obs[44] < 60:
            return 15, 'give_fluids'  # GiveFluids
        else:
            return 6, 'disability'  # ExamineDisability
    elif state == 'give_fluids':
        return 6, 'disability'  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure'  # ExamineExposure
    elif state == 'exposure':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        if is_stabilized(obs):
            return 48, 'finish'  # Finish
        elif obs[46] < 65 or obs[44] < 20:
            return 17, 'cpr'  # StartChestCompression
        else:
            return 16, 'monitor'  # ViewMonitor
    elif state == 'cpr':
        if obs[46] >= 65 and obs[44] >= 20:
            return 16, 'monitor'  # ViewMonitor
        else:
            return 23, 'cpr'  # ResumeCPR
    return 16, 'monitor'  # ViewMonitor as default

state = 'start'
for _ in range(350):
    observations = input()
    obs = parse_observations(observations)
    action, state = choose_action(obs, state)
    print(action)
    sys.stdout.flush()
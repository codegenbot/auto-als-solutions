import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if state == 'initial':
        return 8, 'response'  # ExamineResponse
    
    elif state == 'response':
        if obs[0] > 0 or obs[1] > 0 or obs[2] > 0:
            return 3, 'airway'  # ExamineAirway
        else:
            return 1, 'signs_of_life'  # CheckSignsOfLife
    
    elif state == 'signs_of_life':
        return 2, 'rhythm'  # CheckRhythm
    
    elif state == 'rhythm':
        if obs[28] > 0 or obs[29] > 0 or obs[30] > 0 or obs[31] > 0:
            return 3, 'airway'  # ExamineAirway
        else:
            return 17, 'cpr'  # StartChestCompression
    
    elif state == 'airway':
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            return 35, 'airway_maneuvers'  # PerformAirwayManoeuvres
        else:
            return 4, 'breathing'  # ExamineBreathing
    
    elif state == 'airway_maneuvers':
        return 4, 'breathing'  # ExamineBreathing
    
    elif state == 'breathing':
        if obs[25] == 0:
            return 25, 'use_sats_probe'  # UseSatsProbe
        elif obs[38] < 0.88:
            return 30, 'oxygen'  # UseNonRebreatherMask
        else:
            return 5, 'circulation'  # ExamineCirculation
    
    elif state in ['use_sats_probe', 'oxygen']:
        return 16, 'view_monitor'  # ViewMonitor
    
    elif state == 'view_monitor':
        if obs[38] < 0.88:
            return 30, 'oxygen'  # UseNonRebreatherMask
        else:
            return 5, 'circulation'  # ExamineCirculation
    
    elif state == 'circulation':
        if obs[37] == 0:
            return 27, 'bp_cuff'  # UseBloodPressureCuff
        elif obs[37] < 60:
            return 15, 'fluids'  # GiveFluids
        else:
            return 6, 'disability'  # ExamineDisability
    
    elif state in ['bp_cuff', 'fluids']:
        return 16, 'view_monitor'  # ViewMonitor
    
    elif state == 'disability':
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            return 6, 'disability'  # ExamineDisability again
        else:
            return 7, 'exposure'  # ExamineExposure
    
    elif state == 'exposure':
        if obs[38] >= 0.88 and obs[35] >= 8 and obs[37] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'view_monitor'  # ViewMonitor
    
    elif state == 'cpr':
        if obs[28] > 0 or obs[29] > 0 or obs[30] > 0 or obs[31] > 0:
            return 23, 'post_cpr'  # ResumeCPR
        else:
            return 17, 'cpr'  # StartChestCompression
    
    elif state == 'post_cpr':
        return 16, 'view_monitor'  # ViewMonitor
    

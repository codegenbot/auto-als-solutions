import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state, action_counts, step):
    if obs[7] > 0 or obs[46] < 65 or obs[45] < 20:  # BreathingNone or critical condition
        return 17, 'cpr', action_counts  # StartChestCompression

    if state == 'cpr':
        if action_counts['StartChestCompression'] < 5:
            action_counts['StartChestCompression'] += 1
            return 17, state, action_counts
        elif obs[24] == 0:
            return 28, state, action_counts  # AttachDefibPads
        elif obs[1] == 0:
            return 2, 'assess_rhythm', action_counts  # CheckRhythm
    
    if state == 'assess_rhythm':
        if obs[38] > 0:  # VF rhythm detected
            return 40, 'defibrillate', action_counts  # DefibrillatorCharge
        else:
            return 23, 'cpr', action_counts  # ResumeCPR

    if state == 'defibrillate':
        return 41, 'cpr', action_counts  # DefibrillatorCurrentUp

    if state == 'start':
        if obs[40] == 0:
            return 25, state, action_counts  # UseSatsProbe
        elif obs[39] == 0:
            return 27, state, action_counts  # UseBloodPressureCuff
        elif obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            return 8, 'airway', action_counts  # ExamineResponse
    
    if state == 'airway':
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            return 3, 'breathing', action_counts  # ExamineAirway
    
    if state == 'breathing':
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            return 4, 'circulation', action_counts  # ExamineBreathing
    
    if state == 'circulation':
        if obs[16] == 0 and obs[17] == 0:
            return 5, 'disability', action_counts  # ExamineCirculation
    
    if state == 'disability':
        if obs[23] == 0 and obs[24] == 0:
            return 6, 'exposure', action_counts  # ExamineDisability
    
    if state == 'exposure':
        if obs[25] == 0 and obs[26] == 0:
            return 7, 'monitor', action_counts  # ExamineExposure
    
    if state == 'monitor':
        return 16, 'treat', action_counts  # ViewMonitor
    
    if state == 'treat':
        if obs[46] < 88 and obs[40] > 0:
            if action_counts['UseNonRebreatherMask'] < 3:
                action_counts['UseNonRebreatherMask'] += 1
                return 30, state, action_counts  # UseNonRebreatherMask
        elif obs[45] < 60 and obs[39] > 0:
            if action_counts['GiveFluids'] < 3:
                action_counts['GiveFluids'] += 1
                return 15, state, action_counts  # GiveFluids
        elif obs[41] > 100:  # Tachycardia
            if action_counts['GiveAdenosine'] < 2:
                action_counts['GiveAdenosine'] += 1
                return 9, state, action_counts  # GiveAdenosine
        elif obs[46] >= 88 and obs[45]
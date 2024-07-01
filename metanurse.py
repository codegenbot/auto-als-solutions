import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def check_stabilized(obs):
    return (obs[46] >= 88 and obs[41] >= 8 and obs[45] >= 60)

def choose_action(obs, state, action_counts, step):
    if obs[46] < 65 or obs[45] < 20:
        return 17, 'cardiac_arrest', action_counts  # StartChestCompression

    if state == 'cardiac_arrest':
        if action_counts['StartChestCompression'] < 1:
            action_counts['StartChestCompression'] += 1
            return 17, state, action_counts  # StartChestCompression
        elif action_counts['UseMonitorPads'] < 1:
            action_counts['UseMonitorPads'] += 1
            return 24, state, action_counts  # UseMonitorPads
        elif action_counts['CheckRhythm'] < 1:
            action_counts['CheckRhythm'] += 1
            return 2, 'treat_rhythm', action_counts  # CheckRhythm
    
    if state == 'treat_rhythm':
        if obs[38] > 0:  # VF detected
            if action_counts['DefibrillatorCharge'] < 1:
                action_counts['DefibrillatorCharge'] += 1
                return 40, state, action_counts  # DefibrillatorCharge
            else:
                return 41, 'post_shock', action_counts  # DefibrillatorCurrentUp (Shock)
        else:
            return 23, 'start', action_counts  # ResumeCPR

    if obs[7] > 0:  # BreathingNone detected
        if action_counts['UseBagValveMask'] < 3:
            action_counts['UseBagValveMask'] += 1
            return 29, state, action_counts  # UseBagValveMask
        else:
            return 17, 'cardiac_arrest', action_counts  # StartChestCompression
    
    if state == 'start':
        if obs[40] == 0:
            return 25, state, action_counts  # UseSatsProbe
        elif obs[39] == 0:
            return 27, state, action_counts  # UseBloodPressureCuff
        elif obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            return 8, 'airway', action_counts  # ExamineResponse
    elif state == 'airway':
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            return 3, 'breathing', action_counts  # ExamineAirway
    elif state == 'breathing':
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            return 4, 'circulation', action_counts  # ExamineBreathing
    elif state == 'circulation':
        if obs[16] == 0 and obs[17] == 0:
            return 5, 'disability', action_counts  # ExamineCirculation
    elif state == 'disability':
        if obs[23] == 0 and obs[24] == 0:
            return 6, 'exposure', action_counts  # ExamineDisability
    elif state == 'exposure':
        if obs[25] == 0 and obs[26] == 0:
            return 7, 'monitor', action_counts  # ExamineExposure
    elif state == 'monitor':
        return 16, 'treat', action_counts  # ViewMonitor
    elif state == 'treat':
        if obs[46] < 88 and obs[40] > 0:
            if action_counts['UseNonRebreatherMask'] < 3:
                action_counts['UseNonRebreatherMask
import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state, action_counts, step):
    if step >= 349:
        return 48, 'finish', action_counts

    if obs[17] > 0 or obs[45] < 20:  # RadialPulseNonPalpable or MAP < 20
        return handle_cardiac_arrest(obs, action_counts)

    if state == 'start':
        if obs[24] == 0:
            return 25, 'setup', action_counts  # UseSatsProbe
    elif state == 'setup':
        if obs[39] == 0:
            return 27, 'assess', action_counts  # UseBloodPressureCuff
        return 8, 'assess', action_counts  # ExamineResponse
    elif state == 'assess':
        if obs[3] == 0:
            return 3, state, action_counts  # ExamineAirway
        if obs[7] == 0:
            return 4, state, action_counts  # ExamineBreathing
        if obs[16] == 0:
            return 5, state, action_counts  # ExamineCirculation
        if obs[20] == 0:
            return 6, state, action_counts  # ExamineDisability
        if obs[25] == 0:
            return 7, 'treat', action_counts  # ExamineExposure
    elif state == 'treat':
        if obs[46] < 88 and obs[40] > 0:
            if action_counts['UseNonRebreatherMask'] < 3:
                action_counts['UseNonRebreatherMask'] += 1
                return 30, state, action_counts  # UseNonRebreatherMask
        if obs[45] < 60 and obs[39] > 0:
            if action_counts['UseVenflonIVCatheter'] == 0:
                action_counts['UseVenflonIVCatheter'] = 1
                return 14, state, action_counts  # UseVenflonIVCatheter
            if action_counts['GiveFluids'] < 3:
                action_counts['GiveFluids'] += 1
                return 15, state, action_counts  # GiveFluids
        if obs[7] > 0:  # BreathingNone
            if action_counts['UseBagValveMask'] < 3:
                action_counts['UseBagValveMask'] += 1
                return 29, state, action_counts  # UseBagValveMask
        if obs[41] < 8 or obs[41] > 20:  # Abnormal respiratory rate
            return 4, state, action_counts  # ExamineBreathing
        if obs[46] >= 88 and obs[45] >= 60 and 8 <= obs[41] <= 20:
            return 48, 'finish', action_counts  # Finish

    return 16, state, action_counts  # ViewMonitor as default action

def handle_cardiac_arrest(obs, action_counts):
    if action_counts['StartChestCompression'] == 0:
        action_counts['StartChestCompression'] = 1
        return 17, 'cpr', action_counts  # StartChestCompression
    if action_counts['CheckRhythm'] == 0:
        action_counts['CheckRhythm'] = 1
        return 2, 'cpr', action_counts  # CheckRhythm
    if obs[38] > 0:  # HeartRhythmVF
        if action_counts['AttachDefibPads'] == 0:
            action_counts['AttachDefibPads'] = 1
            return 28, 'cpr', action_counts  # AttachDefibPads
        if action_counts['TurnOnDefibrillator'] == 0:
            action_counts['TurnOnDefibrillator'] = 1
            return
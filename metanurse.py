import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state, action_counts, step):
    if obs[17] > 0 or obs[45] < 20:  # RadialPulseNonPalpable or MAP < 20
        return 17, 'cardiac_arrest', action_counts  # StartChestCompression

    if state == 'cardiac_arrest':
        if action_counts['StartChestCompression'] % 5 == 0:
            return 2, state, action_counts  # CheckRhythm
        if obs[38] > 0:  # HeartRhythmVF
            if action_counts['AttachDefibPads'] == 0:
                action_counts['AttachDefibPads'] = 1
                return 28, state, action_counts  # AttachDefibPads
            return 40, state, action_counts  # DefibrillatorCharge
        action_counts['StartChestCompression'] += 1
        return 17, state, action_counts  # StartChestCompression

    if obs[7] > 0:  # BreathingNone
        if action_counts['UseBagValveMask'] < 3:
            action_counts['UseBagValveMask'] += 1
            return 29, state, action_counts  # UseBagValveMask

    if state == 'start':
        if obs[40] == 0:
            return 25, 'equipment', action_counts  # UseSatsProbe
        if obs[39] == 0:
            return 27, 'equipment', action_counts  # UseBloodPressureCuff
        return 8, 'airway', action_counts  # ExamineResponse

    if state == 'equipment':
        if obs[40] == 0:
            return 25, state, action_counts  # UseSatsProbe
        if obs[39] == 0:
            return 27, 'airway', action_counts  # UseBloodPressureCuff
        return 8, 'airway', action_counts  # ExamineResponse

    if state == 'airway':
        return 3, 'breathing', action_counts  # ExamineAirway

    if state == 'breathing':
        return 4, 'circulation', action_counts  # ExamineBreathing

    if state == 'circulation':
        if action_counts['UseVenflonIVCatheter'] == 0:
            action_counts['UseVenflonIVCatheter'] = 1
            return 14, state, action_counts  # UseVenflonIVCatheter
        return 5, 'disability', action_counts  # ExamineCirculation

    if state == 'disability':
        return 6, 'exposure', action_counts  # ExamineDisability

    if state == 'exposure':
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
        elif obs[46] >= 88 and obs[45] >= 60 and obs[41] >= 8:
            return 48, 'finish', action_counts  # Finish

    if step > 300:
        return 48, 'finish', action_counts  # Finish to avoid timeout

    return 16, state, action_counts  # View
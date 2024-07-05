import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state):
    if state['steps'] >= 349:
        return 48  # Finish if reaching step limit

    if obs[17] > 0.5 or obs[46] > 0.5 and obs[-1] < 65 or obs[45] > 0.5 and obs[-2] < 20:
        state['cpr_needed'] = True
        return handle_cpr(state)

    if not state['monitor_attached']:
        if obs[24] < 0.5:
            state['monitor_attached'] = True
            return 24  # UseMonitorPads
        if obs[25] < 0.5:
            return 25  # UseSatsProbe
        if obs[26] < 0.5:
            return 26  # UseAline
        if obs[27] < 0.5:
            return 27  # UseBloodPressureCuff
        state['monitor_attached'] = True

    if not state['vitals_checked']:
        return 16  # ViewMonitor

    if obs[46] > 0.5 and obs[-1] < 88:
        return 30  # UseNonRebreatherMask

    if obs[45] > 0.5 and obs[-2] < 60:
        return 15  # GiveFluids

    if obs[40] > 0.5 and obs[-7] < 8:
        return 29  # UseBagValveMask

    if not state['abcde_complete']:
        return complete_abcde(obs, state)

    if obs[38] > 0.5 and obs[-8] > 150 and state['vitals_stable']:
        return 9  # GiveAdenosine

    if (obs[3] > 0.5 and
        obs[46] > 0.5 and obs[-1] >= 88 and
        obs[40] > 0.5 and obs[-7] >= 8 and
        obs[45] > 0.5 and obs[-2] >= 60):
        return 48  # Finish

    return 16  # ViewMonitor (default action)

def complete_abcde(obs, state):
    if not state['airway_checked']:
        state['airway_checked'] = True
        return 3  # ExamineAirway
    if not state['breathing_checked']:
        state['breathing_checked'] = True
        return 4  # ExamineBreathing
    if not state['circulation_checked']:
        state['circulation_checked'] = True
        return 5  # ExamineCirculation
    if not state['disability_checked']:
        state['disability_checked'] = True
        return 6  # ExamineDisability
    if not state['exposure_checked']:
        state['exposure_checked'] = True
        return 7  # ExamineExposure
    state['abcde_complete'] = True
    return 16  # ViewMonitor

def handle_cpr(state):
    if not state['cpr_started']:
        state['cpr_started'] = True
        return 17  # StartChestCompression
    if not state['defib_attached']:
        state['defib_attached'] = True
        return 28  # AttachDefibPads
    if not state['defib_on']:
        state['defib_on'] = True
        return 39  # TurnOnDefibrillator
    if not state['rhythm_checked']:
        state['rhythm_checked'] = True
        return 2  # CheckRhythm
    return 23  # ResumeCPR

state = {
    'steps': 0,
    'monitor_attached': False,
    'vitals_checked': False,
    'abcde_complete': False,
    'airway_checked': False,
    'breathing_checked': False,
    'circulation_checked': False,
    'disability_checked': False,
    'exposure_checked': False,
    'vitals_stable': False,
    'cpr_needed
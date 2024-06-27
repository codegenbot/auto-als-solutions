import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

class State:
    def __init__(self):
        self.airway_checked = False
        self.breathing_checked = False
        self.circulation_checked = False
        self.disability_checked = False
        self.exposure_checked = False
        self.sats_probe_used = False
        self.bp_cuff_used = False
        self.fluids_given = False
        self.monitor_viewed = False
        self.oxygen_given = False
        self.last_abcde_check = 0

def choose_action(observations, state, step):
    obs = parse_observations(observations)
    
    # Check if measurements are available
    sats_available = obs[39] > 0 and obs[45] > 0
    bp_available = obs[41] > 0 and obs[46] > 0
    resp_available = obs[40] > 0 and obs[46] > 0
    heart_rate_available = obs[38] > 0 and obs[44] > 0
    
    # Critical conditions
    if sats_available and obs[45] < 65:
        return 17  # StartChestCompression
    if bp_available and obs[46] < 20:
        return 17  # StartChestCompression
    if obs[7] > 0.5:  # BreathingNone
        return 17  # StartChestCompression
    
    # Periodic ABCDE reassessment
    if step - state.last_abcde_check >= 20:
        state.airway_checked = False
        state.breathing_checked = False
        state.circulation_checked = False
        state.disability_checked = False
        state.exposure_checked = False
        state.last_abcde_check = step
    
    # ABCDE assessment
    if not state.airway_checked:
        state.airway_checked = True
        return 3  # ExamineAirway
    
    if not state.breathing_checked:
        state.breathing_checked = True
        return 4  # ExamineBreathing
    
    if not state.circulation_checked:
        state.circulation_checked = True
        return 5  # ExamineCirculation
    
    if not state.disability_checked:
        state.disability_checked = True
        return 6  # ExamineDisability
    
    if not state.exposure_checked:
        state.exposure_checked = True
        return 7  # ExamineExposure
    
    # Vital signs
    if not state.sats_probe_used:
        state.sats_probe_used = True
        return 25  # UseSatsProbe
    
    if not state.bp_cuff_used:
        state.bp_cuff_used = True
        return 27  # UseBloodPressureCuff
    
    if not state.monitor_viewed and (state.sats_probe_used or state.bp_cuff_used):
        state.monitor_viewed = True
        return 16  # ViewMonitor
    
    # Interventions based on vital signs
    if not state.oxygen_given and (sats_available and obs[45] < 94):
        state.oxygen_given = True
        return 30  # UseNonRebreatherMask
    
    if not state.fluids_given and ((resp_available and obs[46] < 8) or (bp_available and obs[46] < 60)):
        state.fluids_given = True
        return 15  # GiveFluids
    
    if heart_rate_available and obs[44] > 150:
        return 9  # GiveAdenosine
    
    # Check if patient is stabilized
    if (sats_available and obs[45] >= 88 and
        resp_available and obs[46] >= 8 and
        bp_available and obs[46] >= 60):
        return 48  # Finish
    
    return 0  # DoNothing if no specific action is needed

state = State()
step = 0
while step <
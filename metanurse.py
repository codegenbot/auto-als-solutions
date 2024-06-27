import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

class PatientState:
    def __init__(self):
        self.airway_checked = False
        self.breathing_checked = False
        self.circulation_checked = False
        self.disability_checked = False
        self.exposure_checked = False
        self.sats_probe_attached = False
        self.bp_cuff_attached = False
        self.oxygen_given = False

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    # Check if vital signs are available and meet criteria
    sats = obs[51] if obs[39] > 0 and state.sats_probe_attached else None
    resp_rate = obs[52] if obs[40] > 0 else None
    map_value = obs[50] if obs[41] > 0 and state.bp_cuff_attached else None

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

    # Attach monitoring equipment
    if not state.sats_probe_attached:
        state.sats_probe_attached = True
        return 25  # UseSatsProbe

    if not state.bp_cuff_attached:
        state.bp_cuff_attached = True
        return 27  # UseBloodPressureCuff

    # Check vital signs and intervene if necessary
    if sats is not None and sats < 88 and not state.oxygen_given:
        state.oxygen_given = True
        return 30  # UseNonRebreatherMask

    if (resp_rate is not None and resp_rate < 8) or (map_value is not None and map_value < 60):
        return 15  # GiveFluids

    # Check for critical conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression

    # If all checks pass and vitals are stable, patient is stabilized
    if (sats is not None and sats >= 88) and (resp_rate is not None and resp_rate >= 8) and (map_value is not None and map_value >= 60):
        return 48  # Finish

    # If we're here, we need more information
    return 16  # ViewMonitor

state = PatientState()
step = 0
while step < 350:
    observations = input().strip()
    action = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
    
    if action == 48:  # Finish
        break
    
    step += 1
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
        self.sats_measured = False
        self.bp_measured = False
        self.rhythm_checked = False

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    # Check for cardiac arrest
    if obs[7] > 0 and obs[17] > 0:  # No breathing and no pulse
        return 17  # StartChestCompression

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

    # Check vitals
    if not state.sats_measured:
        state.sats_measured = True
        return 25  # UseSatsProbe
    
    if not state.bp_measured:
        state.bp_measured = True
        return 27  # UseBloodPressureCuff
    
    if not state.rhythm_checked:
        state.rhythm_checked = True
        return 2  # CheckRhythm

    # Interventions based on measurements
    if obs[51] < 88 and obs[44] > 0:  # Sats < 88% and measurement is recent
        return 30  # UseNonRebreatherMask
    
    if (obs[52] < 8 and obs[45] > 0) or (obs[50] < 60 and obs[43] > 0):  # RR < 8 or MAP < 60
        return 15  # GiveFluids

    # Check if patient is stabilized
    if (obs[51] >= 88 and obs[44] > 0) and (obs[52] >= 8 and obs[45] > 0) and (obs[50] >= 60 and obs[43] > 0):
        return 48  # Finish

    # Default action if no specific action is needed
    return 0  # DoNothing

state = State()
step = 0
while step < 350:
    observations = input().strip()
    action = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
    
    if action == 48:  # Finish
        break
    
    step += 1
import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

class State:
    def __init__(self):
        self.step = 0
        self.airway_drawer_open = False
        self.breathing_drawer_open = False
        self.circulation_drawer_open = False
        self.sats_probe_attached = False
        self.bp_cuff_attached = False
        self.bag_valve_mask_ready = False
        self.airway_checked = False
        self.breathing_checked = False
        self.circulation_checked = False
        self.disability_checked = False
        self.exposure_checked = False

def choose_action(obs, state):
    state.step += 1
    if state.step > 350:
        return 48  # Finish due to timeout

    if not state.airway_drawer_open:
        state.airway_drawer_open = True
        return 18  # OpenAirwayDrawer
    elif not state.breathing_drawer_open:
        state.breathing_drawer_open = True
        return 19  # OpenBreathingDrawer
    elif not state.circulation_drawer_open:
        state.circulation_drawer_open = True
        return 20  # OpenCirculationDrawer
    elif not state.sats_probe_attached:
        state.sats_probe_attached = True
        return 25  # UseSatsProbe
    elif not state.bp_cuff_attached:
        state.bp_cuff_attached = True
        return 27  # UseBloodPressureCuff
    elif not state.bag_valve_mask_ready:
        state.bag_valve_mask_ready = True
        return 29  # UseBagValveMask

    if not state.airway_checked:
        state.airway_checked = True
        return 3  # ExamineAirway
    elif not state.breathing_checked:
        state.breathing_checked = True
        return 4  # ExamineBreathing
    elif not state.circulation_checked:
        state.circulation_checked = True
        return 5  # ExamineCirculation
    elif not state.disability_checked:
        state.disability_checked = True
        return 6  # ExamineDisability
    elif not state.exposure_checked:
        state.exposure_checked = True
        return 7  # ExamineExposure

    # Check vital signs
    if obs[46] < 0.5 or obs[45] < 0.5 or obs[40] < 0.5:
        return 16  # ViewMonitor

    sats = obs[-1] if obs[46] > 0.5 else 0
    map_value = obs[-2] if obs[45] > 0.5 else 0
    resp_rate = obs[-7] if obs[40] > 0.5 else 0

    if sats < 65 or map_value < 20:
        return 17  # StartChestCompression

    if sats < 88:
        return 30  # UseNonRebreatherMask

    if map_value < 60:
        return 15  # GiveFluids

    if resp_rate < 8:
        return 29  # UseBagValveMask

    # Check if patient is stabilized
    if sats >= 88 and map_value >= 60 and resp_rate >= 8:
        return 48  # Finish

    return 0  # DoNothing

state = State()

for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations, state)
    print(action)
    sys.stdout.flush()
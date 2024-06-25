import sys

# Constants for actions
DO_NOTHING = 0
USE_SATS_PROBE = 25
USE_BP_CUFF = 27
VIEW_MONITOR = 16
EXAMINE_AIRWAY = 3
EXAMINE_BREATHING = 4
EXAMINE_CIRCULATION = 5
USE_BVM = 29
USE_NON_REBREATHER_MASK = 30
START_CHEST_COMPRESSIONS = 17
GIVE_FLUIDS = 15
FINISH = 48


def get_action(observations):
    global step
    step += 1

    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    # Initial checks: gather vital signs
    if step == 1:
        return USE_SATS_PROBE
    if step == 2:
        return USE_BP_CUFF
    if step == 3:
        return VIEW_MONITOR
    if step == 4:
        if resp_rate is None:
            return EXAMINE_BREATHING
        elif map_value is None:
            return USE_BP_CUFF
        elif sats is None:
            return USE_SATS_PROBE

    # Handle critical situations
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return START_CHEST_COMPRESSIONS

    if map_value is not None and map_value < 60:
        return GIVE_FLUIDS
    if resp_rate is not None and resp_rate < 8:
        return USE_BVM
    if sats is not None and sats < 88:
        return USE_NON_REBREATHER_MASK

    # Continue checks based on vital signs
    if resp_rate is None:
        return EXAMINE_BREATHING
    if map_value is None:
        return USE_BP_CUFF
    if sats is None:
        return USE_SATS_PROBE

    # Check if stabilized
    if map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return FINISH

    return DO_NOTHING


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == FINISH:
        break
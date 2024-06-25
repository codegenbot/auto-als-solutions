import sys

# Constants for actions (shortened for brevity)
ACTIONS = {
    "DO_NOTHING": 0, "CHECK_SIGNS_OF_LIFE": 1, "CHECK_RHYTHM": 2, "EXAMINE_AIRWAY": 3,
    "EXAMINE_BREATHING": 4, "EXAMINE_CIRCULATION": 5, "EXAMINE_DISABILITY": 6, "EXAMINE_EXPOSURE": 7,
    "USE_NON_REBREATHER_MASK": 30, "START_CHEST_COMPRESSIONS": 17, "USE_BVM": 29,
    "GIVE_FLUIDS": 15, "FINISH": 48, "USE_SATS_PROBE": 25, "USE_BP_CUFF": 27, "VIEW_MONITOR": 16
}

def get_action(observations):
    global step
    step += 1

    # Unpacking observations
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    cap_glucose = vital_signs_values[2] if vital_signs_time[2] > 0 else None
    temp = vital_signs_values[3] if vital_signs_time[3] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    # Initial checks to gather vital signs
    if step == 1:
        return ACTIONS["USE_SATS_PROBE"]
    elif step == 2:
        return ACTIONS["USE_BP_CUFF"]
    elif step == 3:
        return ACTIONS["VIEW_MONITOR"]

    # Airway assessment (A)
    if events[3] == 0:  # Airway not clear
        return ACTIONS["EXAMINE_AIRWAY"]

    # Breathing assessment (B)
    if sats is not None and sats < 65:
        return ACTIONS["START_CHEST_COMPRESSIONS"]
    elif resp_rate is not None and resp_rate < 8:
        return ACTIONS["USE_BVM"]
    elif sats is not None and sats < 88:
        return ACTIONS["USE_NON_REBREATHER_MASK"]
    elif events[7] == 0:  # BreathingNone observed
        return ACTIONS["START_CHEST_COMPRESSIONS"]

    # Circulation assessment (C)
    if map_value is not None and map_value < 20:
        return ACTIONS["START_CHEST_COMPRESSIONS"]
    elif map_value is not None and map_value < 60:
        return ACTIONS["GIVE_FLUIDS"]

    # Disability (D) - Placeholder for further implementation
    # Exposure (E) - Placeholder for further implementation

    # If all criteria for stabilization are met, finish
    if map_value is not None and map_value >= 60 and resp_rate is not None and resp_rate >= 8 and sats is not None and sats >= 88:
        return ACTIONS["FINISH"]

    return ACTIONS["DO_NOTHING"]

global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == ACTIONS["FINISH"]:
        break
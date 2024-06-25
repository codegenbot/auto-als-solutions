import sys

ACTIONS = {
    "DO_NOTHING": 0,
    "USE_SATS_PROBE": 25,
    "USE_BP_CUFF": 27,
    "VIEW_MONITOR": 16,
    "EXAMINE_AIRWAY": 3,
    "EXAMINE_BREATHING": 4,
    "EXAMINE_CIRCULATION": 5,
    "USE_BVM": 29,
    "USE_NON_REBREATHER_MASK": 30,
    "START_CHEST_COMPRESSIONS": 17,
    "GIVE_FLUIDS": 15,
    "FINISH": 48,
}

sequence = [
    ACTIONS["USE_SATS_PROBE"],
    ACTIONS["USE_BP_CUFF"],
    ACTIONS["VIEW_MONITOR"],
    ACTIONS["EXAMINE_AIRWAY"],
    ACTIONS["EXAMINE_BREATHING"],
    ACTIONS["EXAMINE_CIRCULATION"],
]

def get_action(observations, step, examined):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return ACTIONS["START_CHEST_COMPRESSIONS"]

    if step < len(sequence):
        return sequence[step]

    if events[3] == 0 and not examined["airway"]:
        examined["airway"] = True
        return ACTIONS["EXAMINE_AIRWAY"]

    if resp_rate is None and not examined["breathing"]:
        examined["breathing"] = True
        return ACTIONS["EXAMINE_BREATHING"]
    if resp_rate is not None and resp_rate < 8:
        return ACTIONS["USE_BVM"]

    if map_value is None and not examined["circulation"]:
        examined["circulation"] = True
        return ACTIONS["EXAMINE_CIRCULATION"]
    if map_value is not None and map_value < 60:
        return ACTIONS["GIVE_FLUIDS"]

    if sats is None and not examined["sats"]:
        examined["sats"] = True
        return ACTIONS["USE_SATS_PROBE"]
    if sats is not None and sats < 88:
        return ACTIONS["USE_NON_REBREATHER_MASK"]

    if map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return ACTIONS["FINISH"]

    return ACTIONS["DO_NOTHING"]

step = 0
examined = {"airway": False, "breathing": False, "circulation": False, "sats": False}
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data, step, examined)
    print(action)
    if action == ACTIONS["FINISH"]:
        break
    step += 1
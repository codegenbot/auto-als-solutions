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

INITIAL_ACTION_SEQUENCE = [
    ACTIONS["USE_SATS_PROBE"],
    ACTIONS["USE_BP_CUFF"],
    ACTIONS["VIEW_MONITOR"],
    ACTIONS["EXAMINE_AIRWAY"],
    ACTIONS["EXAMINE_BREATHING"],
    ACTIONS["EXAMINE_CIRCULATION"],
]


def stabilize_patient(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    return events, heart_rate, resp_rate, map_value, sats


def get_critical_action(resp_rate, sats, map_value):
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return ACTIONS["START_CHEST_COMPRESSIONS"]


def correct_airway(events):
    if events[3] == 0:
        return ACTIONS["EXAMINE_AIRWAY"]
    elif events[4] > 0 or events[5] > 0 or events[6] > 0:
        return ACTIONS["USE_BVM"]


def correct_breathing(resp_rate, sats, map_value):
    if resp_rate is not None and resp_rate < 8:
        return ACTIONS["USE_BVM"]
    if resp_rate is None:
        return ACTIONS["EXAMINE_BREATHING"]
    if sats is not None and sats < 88:
        return ACTIONS["USE_NON_REBREATHER_MASK"]
    if sats is None:
        return ACTIONS["USE_SATS_PROBE"]


def correct_circulation(map_value):
    if map_value is not None and map_value < 60:
        return ACTIONS["GIVE_FLUIDS"]
    if map_value is None:
        return ACTIONS["USE_BP_CUFF"]


def get_action(observations, step):
    events, heart_rate, resp_rate, map_value, sats = stabilize_patient(observations)

    if step < len(INITIAL_ACTION_SEQUENCE):
        return INITIAL_ACTION_SEQUENCE[step]

    critical_action = get_critical_action(resp_rate, sats, map_value)
    if critical_action is not None:
        return critical_action

    airway_action = correct_airway(events)
    if airway_action is not None:
        return airway_action

    breathing_action = correct_breathing(resp_rate, sats, map_value)
    if breathing_action is not None:
        return breathing_action

    circulation_action = correct_circulation(map_value)
    if circulation_action is not None:
        return circulation_action

    if (
        map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
        and sats is not None
        and sats >= 88
    ):
        return ACTIONS["FINISH"]

    return ACTIONS["DO_NOTHING"]


step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data, step)
    print(action)
    if action == ACTIONS["FINISH"]:
        break
    step += 1
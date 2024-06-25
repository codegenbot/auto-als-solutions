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
    "PERFORM_JAW_THRUST": 37,
    "USE_YANKAUR_SUCTION": 31,
}

EXAMINE_SEQUENCE = [
    ACTIONS["USE_SATS_PROBE"],
    ACTIONS["USE_BP_CUFF"],
    ACTIONS["VIEW_MONITOR"],
    ACTIONS["EXAMINE_AIRWAY"],
    ACTIONS["EXAMINE_BREATHING"],
    ACTIONS["EXAMINE_CIRCULATION"]
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

def get_critical_action(resp_rate, sats, map_value, events):
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return ACTIONS["START_CHEST_COMPRESSIONS"]
    if events[7] == 1 or (resp_rate is not None and resp_rate < 8):
        return ACTIONS["USE_BVM"]
    return None

def correct_airway(events):
    if events[4]:  # Airway vomit
        return ACTIONS["USE_YANKAUR_SUCTION"]
    if events[5] or events[6]:  # Airway blood or tongue block
        return ACTIONS["PERFORM_JAW_THRUST"]
    return None

def correct_breathing(sats):
    if sats is not None and sats < 88:
        return ACTIONS["USE_NON_REBREATHER_MASK"]
    return None

def correct_circulation(map_value):
    if map_value is not None and map_value < 60:
        return ACTIONS["GIVE_FLUIDS"]
    return None

def get_action(observations, step):
    events, heart_rate, resp_rate, map_value, sats = stabilize_patient(observations)

    if step < len(EXAMINE_SEQUENCE):
        return EXAMINE_SEQUENCE[step]

    critical_action = get_critical_action(resp_rate, sats, map_value, events)
    if critical_action:
        return critical_action

    airway_action = correct_airway(events)
    if airway_action:
        return airway_action

    breathing_action = correct_breathing(sats)
    if breathing_action:
        return breathing_action

    circulation_action = correct_circulation(map_value)
    if circulation_action:
        return circulation_action

    if (
        map_value is not None
        and resp_rate is not None
        and sats is not None
        and map_value >= 60
        and resp_rate >= 8
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
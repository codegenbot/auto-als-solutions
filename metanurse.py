import sys

ACTIONS = {
    "DO_NOTHING": 0,
    "CHECK_SIGNS_OF_LIFE": 1,
    "CHECK_RHYTHM": 2,
    "EXAMINE_AIRWAY": 3,
    "EXAMINE_BREATHING": 4,
    "EXAMINE_CIRCULATION": 5,
    "EXAMINE_DISABILITY": 6,
    "EXAMINE_EXPOSURE": 7,
    "EXAMINE_RESPONSE": 8,
    "GIVE_FLUIDS": 15,
    "VIEW_MONITOR": 16,
    "START_CHEST_COMPRESSIONS": 17,
    "USE_SATS_PROBE": 25,
    "USE_BP_CUFF": 27,
    "USE_BVM": 29,
    "USE_NON_REBREATHER_MASK": 30,
    "PERFORM_JAW_THRUST": 37,
    "USE_YANKAUR_SUCTION": 31,
    "FINISH": 48,
}

SEQUENCE = [
    ACTIONS["USE_SATS_PROBE"],
    ACTIONS["USE_BP_CUFF"],
    ACTIONS["VIEW_MONITOR"]
]

def parse_observations(observations):
    events = observations[:33]
    vital_signs_times = observations[33:40]
    vital_signs_values = observations[40:]

    def get_value(time, value):
        return value if time > 0 else None

    heart_rate = get_value(vital_signs_times[0], vital_signs_values[0])
    resp_rate = get_value(vital_signs_times[1], vital_signs_values[1])
    map_value = get_value(vital_signs_times[4], vital_signs_values[4])
    sats = get_value(vital_signs_times[5], vital_signs_values[5])

    return events, heart_rate, resp_rate, map_value, sats

def get_critical_action(resp_rate, sats, map_value, events):
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return ACTIONS["START_CHEST_COMPRESSIONS"]
    if events[7] > 0.5 or (resp_rate is not None and resp_rate < 8):
        return ACTIONS["USE_BVM"]
    return None

def correct_airway(events):
    if events[4] > 0.5:  # Airway vomit
        return ACTIONS["USE_YANKAUR_SUCTION"]
    if events[5] > 0.5 or events[6] > 0.5:  # Airway blood or tongue block
        return ACTIONS["PERFORM_JAW_THRUST"]
    return ACTIONS["EXAMINE_AIRWAY"]

def correct_breathing(sats):
    if sats is not None and sats < 88:
        return ACTIONS["USE_NON_REBREATHER_MASK"]
    return ACTIONS["EXAMINE_BREATHING"]

def correct_circulation(map_value):
    if map_value is not None and map_value < 60:
        return ACTIONS["GIVE_FLUIDS"]
    return ACTIONS["EXAMINE_CIRCULATION"]

def get_action(observations, step):
    events, heart_rate, resp_rate, map_value, sats = parse_observations(observations)

    if step < len(SEQUENCE):
        return SEQUENCE[step]

    critical_action = get_critical_action(resp_rate, sats, map_value, events)
    if critical_action:
        return critical_action

    airway_action = correct_airway(events)
    if airway_action != ACTIONS["EXAMINE_AIRWAY"]:
        return airway_action

    breathing_action = correct_breathing(sats)
    if breathing_action != ACTIONS["EXAMINE_BREATHING"]:
        return breathing_action

    circulation_action = correct_circulation(map_value)
    if circulation_action != ACTIONS["EXAMINE_CIRCULATION"]:
        return circulation_action

    if (
        map_value is not None and map_value >= 60 and
        resp_rate is not None and resp_rate >= 8 and
        sats is not None and sats >= 88
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
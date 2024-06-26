import sys

ACTIONS = {
    0: "DO_NOTHING",
    1: "START_CHEST_COMPRESSIONS",
    2: "USE_SATS_PROBE",
    3: "USE_BP_CUFF",
    4: "VIEW_MONITOR",
    5: "EXAMINE_AIRWAY",
    6: "EXAMINE_BREATHING",
    7: "EXAMINE_CIRCULATION",
    8: "USE_BVM",
    9: "USE_NON_REBREATHER_MASK",
    10: "GIVE_FLUIDS",
    48: "FINISH",
}

SEQUENCE = [5, 6, 7, 2, 3, 4]


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
        return 1  # START_CHEST_COMPRESSIONS
    if resp_rate is not None and resp_rate < 8:
        return 8  # USE_BVM
    return None


def correct_airway(events):
    if events[4]:  # AirwayVomit
        return 31  # USE_YANKAUR_SUCTION
    if events[5] or events[6]:  # AirwayBlood or AirwayTongue
        return 37  # PERFORM_JAW_THRUST
    return None


def correct_breathing(sats):
    if sats is not None and sats < 88:
        return 9  # USE_NON_REBREATHER_MASK
    return None


def correct_circulation(map_value):
    if map_value is not None and map_value < 60:
        return 10  # GIVE_FLUIDS
    return None


def get_action(observations, step):
    events, heart_rate, resp_rate, map_value, sats = stabilize_patient(observations)

    if step < len(SEQUENCE):
        return SEQUENCE[step]

    critical_action = get_critical_action(resp_rate, sats, map_value)
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
        map_value
        and resp_rate
        and sats
        and map_value >= 60
        and resp_rate >= 8
        and sats >= 88
    ):
        return 48  # FINISH

    return 0  # DO_NOTHING


step = 0
while step < 350:
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data, step)
    print(action)
    if action == 48:  # FINISH
        break
    step += 1
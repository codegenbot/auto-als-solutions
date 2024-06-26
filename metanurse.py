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
    "GIVE_ADENOSINE": 9,
    "GIVE_ADRENALINE": 10,
    "GIVE_AMIODARONE": 11,
    "GIVE_ATROPINE": 12,
    "GIVE_MIDAZOLAM": 13,
    "USE_VENFLON_IV_CATHETER": 14,
    "GIVE_FLUIDS": 15,
    "VIEW_MONITOR": 16,
    "START_CHEST_COMPRESSION": 17,
    "OPEN_AIRWAY_DRAWER": 18,
    "OPEN_BREATHING_DRAWER": 19,
    "OPEN_CIRCULATION_DRAWER": 20,
    "OPEN_DRUGS_DRAWER": 21,
    "BAG_DURING_CPR": 22,
    "RESUME_CPR": 23,
    "USE_MONITOR_PADS": 24,
    "USE_SATS_PROBE": 25,
    "USE_ALINE": 26,
    "USE_BP_CUFF": 27,
    "ATTACH_DEFIB_PADS": 28,
    "USE_BAG_VALVE_MASK": 29,
    "USE_NON_REBREATHER_MASK": 30,
    "USE_YANKEUR_SUCTION_CATHETER": 31,
    "USE_GUEDEL_AIRWAY": 32,
    "TAKE_BLOOD_FOR_ARTERIAL_BLOOD_GAS": 33,
    "TAKE_ROUTINE_BLOODS": 34,
    "PERFORM_AIRWAY_MANOEUVRES": 35,
    "PERFORM_HEAD_TILT_CHIN_LIFT": 36,
    "PERFORM_JAW_THRUST": 37,
    "TAKE_BLOOD_PRESSURE": 38,
    "TURN_ON_DEFIBRILLATOR": 39,
    "DEFIBRILLATOR_CHARGE": 40,
    "DEFIBRILLATOR_CURRENT_UP": 41,
    "DEFIBRILLATOR_CURRENT_DOWN": 42,
    "DEFIBRILLATOR_PACE": 43,
    "DEFIBRILLATOR_PACE_PAUSE": 44,
    "DEFIBRILLATOR_RATE_UP": 45,
    "DEFIBRILLATOR_RATE_DOWN": 46,
    "DEFIBRILLATOR_SYNC": 47,
    "FINISH": 48,
}

STEP_SEQUENCE = [
    ACTIONS["EXAMINE_AIRWAY"],
    ACTIONS["EXAMINE_BREATHING"],
    ACTIONS["EXAMINE_CIRCULATION"],
    ACTIONS["USE_SATS_PROBE"],
    ACTIONS["USE_BP_CUFF"],
    ACTIONS["VIEW_MONITOR"],
]


def parse_observations(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    return events, heart_rate, resp_rate, map_value, sats


def stabilize(observations):
    events, heart_rate, resp_rate, map_value, sats = parse_observations(observations)

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return ACTIONS["START_CHEST_COMPRESSION"]
    if events[7] == 1 or (resp_rate is not None and resp_rate < 8):
        return ACTIONS["USE_BAG_VALVE_MASK"]
    if map_value is not None and map_value < 60:
        return ACTIONS["GIVE_FLUIDS"]
    if sats is not None and sats < 88:
        return ACTIONS["USE_NON_REBREATHER_MASK"]

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


def get_action(observations, step):
    if step < len(STEP_SEQUENCE):
        return STEP_SEQUENCE[step]
    return stabilize(observations)


step = 0
while step < 350:
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data, step)
    print(action)
    if action == ACTIONS["FINISH"]:
        break
    step += 1
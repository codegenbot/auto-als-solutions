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
    "USE_VENFLON_IV_CATHTER": 14,
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
    "USE_BLOOD_PRESSURE_CUFF": 27,
    "ATTACH_DEFIB_PADS": 28,
    "USE_BAG_VALVE_MASK": 29,
    "USE_NON_REBREATHER_MASK": 30,
    "USE_YANKAUR_SUCTION": 31,
    "USE_GUEDEL_AIRWAY": 32,
    "TAKE_BLOOD_GAS": 33,
    "TAKE_ROUTINE_BLOODS": 34,
    "PERFORM_AIRWAY_MANOEUVRES": 35,
    "PERFORM_HEAD_TILT_CHIN_LIFT": 36,
    "PERFORM_JAW_THRUST": 37,
    "TAKE_BLOOD_PRESSURE": 38,
    "TURN_ON_DEFIBRILLATOR": 39,
    "DEFIB_CHARGE": 40,
    "DEFIB_CURRENT_UP": 41,
    "DEFIB_CURRENT_DOWN": 42,
    "DEFIB_PACE": 43,
    "DEFIB_PACE_PAUSE": 44,
    "DEFIB_RATE_UP": 45,
    "DEFIB_RATE_DOWN": 46,
    "DEFIB_SYNC": 47,
    "FINISH": 48,
}

SEQUENCE = [
    ACTIONS["EXAMINE_AIRWAY"],
    ACTIONS["EXAMINE_BREATHING"],
    ACTIONS["EXAMINE_CIRCULATION"],
    ACTIONS["USE_SATS_PROBE"],
    ACTIONS["USE_BLOOD_PRESSURE_CUFF"],
    ACTIONS["VIEW_MONITOR"],
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
        return ACTIONS["START_CHEST_COMPRESSION"]
    if events[7] == 1 or (resp_rate is not None and resp_rate < 8):
        return ACTIONS["USE_BAG_VALVE_MASK"]
    return None

def correct_airway(events):
    if events[5]:
        return ACTIONS["USE_YANKAUR_SUCTION"]
    if events[6]:
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
    if step < len(SEQUENCE):
        return SEQUENCE[step]
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
    if map_value is not None and resp_rate is not None and sats is not None and map_value >= 60 and resp_rate >= 8 and sats >= 88:
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
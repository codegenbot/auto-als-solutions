import sys
from math import exp

ACTIONS = list(range(49))

INITIAL_SEQUENCE = [
    ACTIONS[25],  # USE_SATS_PROBE
    ACTIONS[27],  # USE_BP_CUFF
    ACTIONS[16],  # VIEW_MONITOR
    ACTIONS[3],   # EXAMINE_AIRWAY
    ACTIONS[4],   # EXAMINE_BREATHING
    ACTIONS[5],   # EXAMINE_CIRCULATION
]

def stabilize_patient_state(observations):
    events, vitals_time, vitals_values = observations[:33], observations[33:40], observations[40:]
    heart_rate = vitals_values[0] if vitals_time[0] > 0 else None
    resp_rate = vitals_values[1] if vitals_time[1] > 0 else None
    map_value = vitals_values[4] if vitals_time[4] > 0 else None
    sats = vitals_values[5] if vitals_time[5] > 0 else None
    return events, heart_rate, resp_rate, map_value, sats

def get_critical_action(resp_rate, sats, map_value):
    if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
        return ACTIONS[17]  # START_CHEST_COMPRESSIONS

def manage_airway(events):
    if events[7]:  # BreathingNone
        if events[4]:  # Airway Vomit
            return ACTIONS[31]  # USE_YANKAUR_SUCTION
        elif events[5] or events[6]:  # Airway Blood or Tongue
            return ACTIONS[37]  # PERFORM_JAW_THRUST
        return ACTIONS[29]  # USE_BVM
    return ACTIONS[3]  # EXAMINE_AIRWAY

def manage_breathing(resp_rate, sats):
    if resp_rate is not None and resp_rate < 8:
        return ACTIONS[29]  # USE_BVM
    if sats is not None and sats < 88:
        return ACTIONS[30]  # USE_NON_REBREATHER_MASK
    return ACTIONS[4]  # EXAMINE_BREATHING

def manage_circulation(map_value):
    if map_value is not None and map_value < 60:
        return ACTIONS[15]  # GIVE_FLUIDS
    return ACTIONS[5]  # EXAMINE_CIRCULATION

def get_action(observations, step):
    events, heart_rate, resp_rate, map_value, sats = stabilize_patient_state(observations)
    if step < len(INITIAL_SEQUENCE):
        return INITIAL_SEQUENCE[step]
    critical_action = get_critical_action(resp_rate, sats, map_value)
    if critical_action:
        return critical_action
    airway_action = manage_airway(events)
    if airway_action != ACTIONS[3]:
        return airway_action
    breathing_action = manage_breathing(resp_rate, sats)
    if breathing_action != ACTIONS[4]:
        return breathing_action
    circulation_action = manage_circulation(map_value)
    if circulation_action != ACTIONS[5]:
        return circulation_action
    if map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return ACTIONS[48]  # FINISH
    return ACTIONS[0]  # DO_NOTHING

step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data, step)
    print(action)
    if action == ACTIONS[48]:  # FINISH
        break
    step += 1
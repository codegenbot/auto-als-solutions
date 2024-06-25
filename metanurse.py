import sys

DO_NOTHING = 0
USE_SATS_PROBE = 25
USE_BP_CUFF = 27
VIEW_MONITOR = 16
EXAMINE_AIRWAY = 3
EXAMINE_BREATHING = 4
EXAMINE_CIRCULATION = 5
EXAMINE_DISABILITY = 6
EXAMINE_EXPOSURE = 7
USE_BVM = 29
USE_NON_REBREATHER_MASK = 30
START_CHEST_COMPRESSIONS = 17
GIVE_FLUIDS = 15
PERFORM_AIRWAY_MANOEUVRES = 35
USE_GUEDEL_AIRWAY = 32
FINISH = 48

def get_action(observations, step):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    cap_glucose = vital_signs_values[2] if vital_signs_time[2] > 0 else None
    temperature = vital_signs_values[3] if vital_signs_time[3] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None
    measured_resps = vital_signs_values[6] if vital_signs_time[6] > 0 else None

    if step == 1:
        return USE_SATS_PROBE
    if step == 2:
        return USE_BP_CUFF
    if step == 3:
        return VIEW_MONITOR

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return START_CHEST_COMPRESSIONS

    if resp_rate is None:
        return EXAMINE_BREATHING
    if map_value is None:
        return USE_BP_CUFF
    if sats is None:
        return USE_SATS_PROBE
    if events[3] == 0:
        return EXAMINE_AIRWAY

    if events[6] > 0:
        return PERFORM_AIRWAY_MANOEUVRES
    if events[4] > 0 or events[5] > 0:
        return USE_GUEDEL_AIRWAY
    if events[7] > 0:
        return USE_BVM

    if map_value is not None and map_value < 60:
        return GIVE_FLUIDS
    if sats is not None and sats < 88:
        return USE_NON_REBREATHER_MASK

    if map_value is not None and map_value >= 60 and resp_rate is not None and resp_rate >= 8 and sats is not None and sats >= 88:
        return FINISH

    return DO_NOTHING

step = 0

for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    step += 1
    action = get_action(input_data, step)
    print(action)
    if action == FINISH:
        break
import sys

# Constants for actions
ACTION_SEQ = [
    25, 27, 16, 3, 4, 5  # Initial ABCDE checks
]
DO_NOTHING, USE_SATS_PROBE, USE_BP_CUFF, VIEW_MONITOR = 0, 25, 27, 16
EXAMINE_AIRWAY, EXAMINE_BREATHING, EXAMINE_CIRCULATION = 3, 4, 5
USE_BVM, GIVE_FLUIDS, FINISH, START_CHEST_COMPRESSIONS = 29, 15, 48, 17

step = 0

def get_action(observations):
    global step
    step += 1

    events = observations[:33]
    vital_time = observations[33:40]
    vital_values = observations[40:]

    hr = vital_values[0] if vital_time[0] else None
    rr = vital_values[1] if vital_time[1] else None
    map_val = vital_values[4] if vital_time[4] else None
    sats = vital_values[5] if vital_time[5] else None

    if step <= len(ACTION_SEQ):
        return ACTION_SEQ[step - 1]

    if (sats is not None and sats < 65) or (map_val is not None and map_val < 20):
        return START_CHEST_COMPRESSIONS

    if events[3] == 0:  # AirwayClear not confirmed
        return EXAMINE_AIRWAY
    if events[8] > 0:  # Breathing issues
        return USE_BVM
    if rr is not None and rr < 8:
        return USE_BVM
    if map_val is not None and map_val < 60:
        return GIVE_FLUIDS
    if sats is not None and sats < 88:
        return USE_BVM

    if rr is None:
        return EXAMINE_BREATHING
    if map_val is None:
        return USE_BP_CUFF
    if sats is None:
        return USE_SATS_PROBE

    if map_val >= 60 and rr >= 8 and sats >= 88:
        return FINISH

    return DO_NOTHING

for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == FINISH:
        break
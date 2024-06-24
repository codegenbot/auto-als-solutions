import sys
import math

def get_action(observations):
    # Extract the relevant observations
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    # Extract specific vital signs
    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    # Sequence of setup actions
    global step
    if step == 1:
        return 25  # UseSatsProbe
    elif step == 2:
        return 27  # UseBloodPressureCuff

    # Check for cardiac arrest conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression

    # Check if the patient is already stabilized
    if (
        (sats is not None and sats >= 88)
        and (resp_rate is not None and resp_rate >= 8)
        and (map_value is not None and map_value >= 60)
    ):
        return 48  # Finish

    # Perform ABCDE assessment
    if events[3] == 0:  # AirwayClear
        return 3  # ExamineAirway

    if events[7] > 0 or events[8] > 0 or events[9] > 0:  # Breathing issues
        return 4  # ExamineBreathing

    if map_value is None:
        return 38  # TakeBloodPressure

    if sats is None:
        return 16  # ViewMonitor

    # Default to checking signs of life
    return 1  # CheckSignsOfLife

global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    step += 1
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
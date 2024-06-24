import sys


def get_action(observations):
    global step
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if step == 1:
        return 3  # ExamineAirway
    elif step == 2:
        return 4  # ExamineBreathing
    elif step == 3:
        return 5  # ExamineCirculation
    elif step == 4:
        return 6  # ExamineDisability
    elif step == 5:
        return 7  # ExamineExposure

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression

    if map_value is None:
        return 38  # TakeBloodPressure

    if sats is None:
        return 25  # UseSatsProbe

    if sats and sats < 88:
        return 30  # UseNonRebreatherMask for oxygenation

    if resp_rate is None or resp_rate < 8:
        return 29  # UseBagValveMask to support breathing

    if map_value and map_value < 60:
        return 15  # GiveFluids to improve MAP

    if (
        (sats is not None and sats >= 88)
        and (resp_rate is not None and resp_rate >= 8)
        and (map_value is not None and map_value >= 60)
    ):
        return 48  # Finish game if stabilized

    return 1  # Default action: CheckSignsOfLife


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    step += 1
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
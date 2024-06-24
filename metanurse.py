import sys


def get_action(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:47]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    global step
    step += 1

    # Priority checks
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression
    if events[7] > 0:  # BreathingNone event
        return 29  # UseBagValveMask

    # Initial assessments
    if step == 1:
        return 3  # ExamineAirway
    if step == 2:
        return 25  # UseSatsProbe
    if step == 3:
        return 27  # UseBloodPressureCuff
    if step == 4:
        return 5  # ExamineBreathing

    # Treatment logic
    if sats is not None and sats < 88:
        return 30  # UseNonRebreatherMask

    if map_value is not None and map_value < 60:
        return 15  # GiveFluids

    if map_value is None or vital_signs_time[4] == 0:
        return 38  # TakeBloodPressure

    if resp_rate is None or resp_rate < 8:
        return 4  # ExamineBreathing

    if (
        (sats is not None and sats >= 88)
        and (resp_rate is not None and resp_rate >= 8)
        and (map_value is not None and map_value >= 60)
    ):
        return 48  # Finish

    return 1  # CheckSignsOfLife


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
import sys


def get_action(observations):
    global step
    step += 1

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
        return 25  # UseSatsProbe
    elif step == 4:
        return 27  # UseBloodPressureCuff
    elif step < 7:
        return 16  # ViewMonitor to get vitals

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression

    if events[7] > 0:  # BreathingNone
        return 22  # BagDuringCPR

    if map_value is None:
        return 38  # TakeBloodPressure

    if sats is None:
        return 25  # UseSatsProbe

    if (
        (sats is not None and sats >= 88)
        and (resp_rate is not None and resp_rate >= 8)
        and (map_value is not None and map_value >= 60)
    ):
        return 48  # Finish game

    if sats < 88:
        return 30  # UseNonRebreatherMask

    if resp_rate is None or resp_rate < 8:
        return 29  # UseBagValveMask

    if map_value < 60:
        return 15  # GiveFluids

    return 1  # CheckSignsOfLife as the default approach


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
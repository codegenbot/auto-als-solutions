import sys

def get_action(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression

    if events[3] == 0:
        return 3  # ExamineAirway
    if resp_rate is None:
        return 4  # ExamineBreathing
    if events[7] > 0:
        return 29  # UseBagValveMask
    if events[11] == 0:
        return 4  # ExamineBreathing
    if map_value is None:
        return 27  # UseBloodPressureCuff
    if vital_signs_time[4] > 0 and map_value < 60:
        return 15  # GiveFluids
    if resp_rate and resp_rate < 8:
        return 29  # UseBagValveMask
    if sats is None:
        return 25  # UseSatsProbe
    if vital_signs_time[5] > 0 and sats < 88:
        return 30  # UseNonRebreatherMask

    if (sats is not None and sats >= 88) and (resp_rate is not None and resp_rate >= 8) and (map_value is not None and map_value >= 60):
        return 48  # Finish

    return 1  # CheckSignsOfLife

for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
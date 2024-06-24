import sys

def get_action(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if not events[3]:  # Check airway
        return 3  # ExamineAirway

    if events[7] or events[8] or events[9]:  # Check if any breathing issues exist
        return 4  # ExamineBreathing

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression if John's condition deteriorates critically

    if sats is None:  # Missing oxygen saturation
        if vital_signs_time[5] == 0:
            return 25  # UseSatsProbe
        return 16  # ViewMonitor

    if map_value is None:  # Missing mean arterial pressure
        if vital_signs_time[4] == 0:
            return 27  # UseBloodPressureCuff
        return 16  # ViewMonitor

    if sats < 88:
        return 30  # UseNonRebreatherMask

    if resp_rate is None:
        if vital_signs_time[1] == 0:
            return 4  # ExamineBreathing
        return 16  # ViewMonitor

    if (resp_rate < 8) and (events[7] == 0):
        return 29  # UseBagValveMask

    if (sats >= 88) and (resp_rate >= 8) and (map_value >= 60):
        return 48  # Finish if stable

    return 1  # CheckSignsOfLife

for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
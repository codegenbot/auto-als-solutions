import sys

def get_action(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:47]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    global step, examined_airway, used_sats_probe, used_bpcuff, viewed_monitor

    step += 1

    if not examined_airway:
        examined_airway = True
        return 3  # ExamineAirway
    if not used_sats_probe:
        used_sats_probe = True
        return 25  # UseSatsProbe
    if not used_bpcuff:
        used_bpcuff = True
        return 27  # UseBloodPressureCuff
    if not viewed_monitor:
        viewed_monitor = True
        return 16  # ViewMonitor

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression

    if events[3] == 0 and step <= 10:
        return 3  # Recheck Airway if not confirmed clear
    
    if map_value is not None and map_value < 60:
        return 15  # GiveFluids
    
    if resp_rate is None or resp_rate < 8:
        return 4  # ExamineBreathing again
    
    if sats is not None and sats < 88:
        return 30  # UseNonRebreatherMask
    
    if (
        (sats is not None and sats >= 88)
        and (resp_rate is not None and resp_rate >= 8)
        and (map_value is not None and map_value >= 60)
    ):
        return 48  # Finish when stabilized
    
    return 1  # CheckSignsOfLife

global step, examined_airway, used_sats_probe, used_bpcuff, viewed_monitor
step = 0
examined_airway = used_sats_probe = used_bpcuff = viewed_monitor = False

for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
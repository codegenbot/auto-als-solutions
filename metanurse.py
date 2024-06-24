import sys

def get_action(observations, step):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20) or events[7] > 0:
        return 17

    if (
        (sats is not None and sats >= 88)
        and (resp_rate is not None and resp_rate >= 8)
        and (map_value is not None and map_value >= 60)
    ):
        return 48
    
    if step == 1:
        return 25  # UseSatsProbe
    elif step == 2:
        return 27  # UseBloodPressureCuff
    elif step == 3:
        return 16  # ViewMonitor
    elif step == 4:
        return 3  # ExamineAirway
    elif events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        return 31  # Use YankeurSucionCatheter
    elif sats is not None and sats < 88:
        return 30  # UseNonRebreatherMask
    elif map_value is None:
        return 38  # TakeBloodPressure
    elif events[7] > 0:
        return 29  # UseBagValveMask 
    elif resp_rate is None or resp_rate < 8:
        return 4  # ExamineBreathing
    elif map_value is not None and map_value < 60:
        return 15  # GiveFluids
    
    return 1  # DoNothing

global step
step = 0

for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    step += 1
    action = get_action(input_data, step)
    print(action)
    if action == 48:
        break
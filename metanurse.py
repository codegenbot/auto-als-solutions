import sys

def get_action(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    global step
    global examined, interventions

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17

    if step == 1 and sats is None:
        return 25
    if step == 2 and map_value is None:
        return 27

    if not examined["Airway"]:
        examined["Airway"] = True
        return 3
    if not examined["Breathing"]:
        examined["Breathing"] = True
        return 4
    if not examined["Circulation"]:
        examined["Circulation"] = True
        return 16
    if not examined["Disability"]:
        examined["Disability"] = True
        return 6
    if not examined["Exposure"]:
        examined["Exposure"] = True
        return 7

    if ((sats is not None and sats < 88) or (resp_rate is not None and resp_rate < 8)) and "oxygen" not in interventions:
        interventions.add("oxygen")
        return 30
    if map_value is not None and map_value < 60 and "fluids" not in interventions:
        interventions.add("fluids")
        return 15

    if (sats is not None and sats >= 88
        and resp_rate is not None and resp_rate >= 8
        and map_value is not None and map_value >= 60):
        return 48

    return 1

global step
global examined, interventions
step = 0
examined = {"Airway": False, "Breathing": False, "Circulation": False, "Disability": False, "Exposure": False}
interventions = set()
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    step += 1
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
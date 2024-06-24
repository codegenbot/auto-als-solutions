import sys

def get_vital_signs(observations):
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]
    return {
        "heart_rate": vital_signs_values[0] if vital_signs_time[0] > 0 else None,
        "resp_rate": vital_signs_values[1] if vital_signs_time[1] > 0 else None,
        "capillary_glucose": vital_signs_values[2] if vital_signs_time[2] > 0 else None,
        "temperature": vital_signs_values[3] if vital_signs_time[3] > 0 else None,
        "map_value": vital_signs_values[4] if vital_signs_time[4] > 0 else None,
        "sats": vital_signs_values[5] if vital_signs_time[5] > 0 else None,
        "resps": vital_signs_values[6] if vital_signs_time[6] > 0 else None
    }

def get_action(step, observations):
    events = observations[:33]
    vitals = get_vital_signs(observations)

    if step == 1:
        return 25
    elif step == 2:
        return 27
    elif step < 6:
        return 16

    if "sats" in vitals and vitals["sats"] < 65 or "map_value" in vitals and vitals["map_value"] < 20:
        return 17

    if vitals["map_value"] is None:
        return 38

    if vitals["sats"] is None:
        return 25

    if (
        "sats" in vitals and vitals["sats"] >= 88 and
        "resp_rate" in vitals and vitals["resp_rate"] >= 8 and
        "map_value" in vitals and vitals["map_value"] >= 60
    ):
        return 48

    if vitals["sats"] is not None and vitals["sats"] < 88:
        return 30

    if events[7] > 0:
        return 29

    if events[3] > 0:
        if events[4] > 0 or events[5] > 0 or events[6] > 0:
            return 31

    if vitals["resp_rate"] is None or vitals["resp_rate"] < 8:
        return 32

    if vitals["map_value"] < 60:
        return 15

    return 1

global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    step += 1
    action = get_action(step, input_data)
    print(action)
    if action == 48:
        break
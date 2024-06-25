import sys


def get_action(observations):
    global step
    step += 1

    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    measured = {
        "heart_rate": vital_signs_values[0] if vital_signs_time[0] > 0 else None,
        "resp_rate": vital_signs_values[1] if vital_signs_time[1] > 0 else None,
        "cap_glucose": vital_signs_values[2] if vital_signs_time[2] > 0 else None,
        "temperature": vital_signs_values[3] if vital_signs_time[3] > 0 else None,
        "map": vital_signs_values[4] if vital_signs_time[4] > 0 else None,
        "sats": vital_signs_values[5] if vital_signs_time[5] > 0 else None,
        "resps": vital_signs_values[6] if vital_signs_time[6] > 0 else None,
    }

    if step == 1:
        return 25  # Use Sats Probe
    elif step == 2:
        return 27  # Use Blood Pressure Cuff
    elif step == 3:
        return 16  # View Monitor

    if (measured["sats"] is not None and measured["sats"] < 65) or (
        measured["map"] is not None and measured["map"] < 20
    ):
        return 17  # Start Chest Compression

    if events[7] > 0 or measured["resp_rate"] == 0:
        return 29  # Use Bag Valve Mask

    if events[3] == 0:
        if events[4] > 0 or events[5] > 0 or events[6] > 0:
            return 31  # Clear Airway (Use Yankeur Suction Catheter)

    if measured["resp_rate"] is not None and measured["resp_rate"] < 8:
        return 29  # Assist Breathing (Use Bag Valve Mask)

    if measured["sats"] is not None and measured["sats"] < 88:
        return 30  # Use Non Rebreather Mask

    if measured["map"] is not None and measured["map"] < 60:
        return 15  # Give Fluids

    if events[21] == 0 and events[22] == 0 and events[23] == 0 and events[24] == 0:
        return 6  # Examine Disability

    if events[25] == 0 and events[26] == 0 and events[27] == 0:
        return 7  # Examine Exposure

    if all(
        [
            measured["map"] is not None and measured["map"] >= 60,
            measured["resp_rate"] is not None and measured["resp_rate"] >= 8,
            measured["sats"] is not None and measured["sats"] >= 88,
        ]
    ):
        return 48  # Finish the scenario

    return 1  # Default to fetching more data if uncertain


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
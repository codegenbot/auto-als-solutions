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
        return 3  # Examine Airway
    if events[3] == 0:
        return 35  # Perform Airway Maneuvers if airway not clear
    if step == 2:
        return 4  # Examine Breathing
    if step == 3:
        return 19  # Open Breathing Drawer
    if step == 4:
        return 25  # Use Sats Probe
    if step == 5:
        return 27  # Use BP Cuff
    if step == 6:
        return 16  # View Monitor

    if step > 6:
        if (sats is not None and sats < 65) or (
            map_value is not None and map_value < 20
        ):
            return 17  # Start Chest Compressions if critical
        if map_value is not None and map_value < 60:
            return 15  # Give Fluids for MAP < 60
        if resp_rate is not None and resp_rate < 8:
            return 29  # Use Bag Valve Mask for low respiration
        if sats is not None and sats < 88:
            return 30  # Use NonRebreather Mask for low sats
        if all(
            [
                resp_rate is not None and resp_rate >= 8,
                map_value is not None and map_value >= 60,
                sats is not None and sats >= 88,
            ]
        ):
            return 48  # Finish if all vitals are stable

    if events[4] > 0 or events[5] > 0 or events[6] > 0:
        return 31  # Use Yankeur Suction Catheter for airway issues

    return 1  # Check signs of life to keep loop active


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
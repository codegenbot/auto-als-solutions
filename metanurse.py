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

    # Initial checks
    if step == 1:
        return 4  # Examine Breathing
    if step == 2:
        return 25  # Use Sats Probe
    if step == 3:
        return 27  # Use BP Cuff
    if step == 4:
        return 16  # View Monitor

    # Critical conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # Start Chest Compressions

    # Airway
    if events[3] == 0 and (events[4] > 0 or events[5] > 0 or events[6] > 0):
        return 31  # Use Yankeur Suction Catheter
    if events[3] == 0:
        return 35  # Perform Airway Manoeuvres

    # Circulation issues
    if map_value is not None and map_value < 60:
        return 15  # Give Fluids

    # Breathing assistance
    if resp_rate is None or resp_rate < 8:
        return 29  # Use Bag Valve Mask
    if resp_rate < 12 or resp_rate > 20:
        return 4  # Examine Breathing

    # Oxygenation aid
    if sats is not None and sats < 88:
        return 30  # Use NonRebreather Mask

    # Continuous monitoring necessity
    if map_value is None or sats is None or resp_rate is None:
        return 16  # View Monitor

    # Stabilization check
    if map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return 48  # Finish if all vitals are stable

    return 1  # Default action to check signs of life


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
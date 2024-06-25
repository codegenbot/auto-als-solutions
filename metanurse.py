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
        return 25  # Use Sats Probe
    if step == 2:
        return 27  # Use Blood Pressure Cuff
    if step == 3:
        return 16  # View Monitor

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # Start Chest Compression

    if map_value is None or sats is None or resp_rate is None:
        return 16  # View Monitor to get vital signs

    if events[3] == 0:  # If airway is not clear, examine airway
        return 3  # Examine Airway

    if events[8] > 0 or events[9] > 0 or events[10] > 0:  # Breathing issues
        if resp_rate < 8:
            return 30  # Use Non-Rebreather Mask
        if resp_rate > 30:
            return 29  # Use Bag Valve Mask
        else:
            return 5  # Examine Breathing

    if map_value is not None and map_value < 60:
        return 15  # Give Fluids

    if sats is not None and sats < 88:
        return 30  # Use Non-Rebreather Mask

    if step >= 4 and map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return 48  # Finish

    return 1  # Check Signs of Life

global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
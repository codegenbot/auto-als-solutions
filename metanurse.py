import sys


def get_action(observations):
    global step
    step += 1

    # Parse observations
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if step == 1:
        return 3  # Examine Airway
    if step == 2:
        return 4  # Examine Breathing
    if step == 3:
        return 19  # Open Breathing Drawer (to get Sats Probe)
    if step == 4:
        return 25  # Use Sats Probe
    if step == 5:
        return 27  # Use BP Cuff
    if step == 6:
        return 16  # View Monitor

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # Start Chest Compressions

    if map_value is not None and map_value < 60:
        if events[17] == 0:
            return 14  # UseVenflonIVCatheter to prepare fluids
        return 15  # Give Fluids for MAP < 60

    if resp_rate is not None and resp_rate < 8:
        return 29  # Use Bag Valve Mask

    if sats is not None and sats < 88:
        return 30  # Use NonRebreather Mask

    # Re-measure vital signs regularly to ensure stabilization
    if step % 10 == 0:
        return 4  # Examine Breathing to verify current condition
    if step % 15 == 0:
        return 27  # Use BP Cuff again if no reading
    if step % 20 == 0:
        return 25  # Use Sats Probe again if no reading

    if all(
        [
            resp_rate is not None and resp_rate >= 8,
            map_value is not None and map_value >= 60,
            sats is not None and sats >= 88,
        ]
    ):
        return 48  # Finish if all vitals are stable

    return 1  # CheckSignsOfLife to keep loop active


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
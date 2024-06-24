import sys

sats_checked = False
map_checked = False
resp_rate_checked = False
airway_checked = False


def get_action(observations):
    global step, sats_checked, map_checked, resp_rate_checked, airway_checked
    step += 1

    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if not sats_checked:
        sats_checked = True
        return 25  # Use Sats Probe
    if not map_checked:
        map_checked = True
        return 27  # Use BP Cuff
    if step in (3, 4, 5, 6):
        return 16  # View Monitor

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # Start Chest Compressions

    if resp_rate is None and not resp_rate_checked:
        resp_rate_checked = True
        return 4  # Examine Breathing
    if map_value is None and not map_checked:
        return 38  # Check Blood Pressure
    if sats is None and not sats_checked:
        return 25  # Use Sats Probe

    if events[3] == 0 and not airway_checked:
        airway_checked = True
        return 3  # Examine Airway

    if map_value < 60:
        return 15  # Give Fluids
    if resp_rate < 8:
        return 29  # Use Bag Valve Mask
    if sats < 88:
        return 30  # Use NonRebreather Mask

    if map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return 48  # Finish

    return 1  # Default action


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
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

    actions = [3, 4, 25, 27, 16]  # Examine Airway, Breathing, Use Sats Probe, BP Cuff, View Monitor

    if step <= len(actions):
        return actions[step - 1]
    
    # Immediate necessary actions
    if (sats and sats < 65) or (map_value and map_value < 20):
        return 17  # Start Chest Compressions

    if events[3] == 0 and any(events[4:7]):  # Airway issues
        return 31  # Use Yankeur Suction Catheter
    if events[3] == 0:
        return 35  # Perform Airway Maneuvers
    
    if map_value is None:
        return 38 # Check Blood Pressure again
    if sats is None:
        return 25 # Use Sats Probe again
    if resp_rate is None:
        return 4  # Examine Breathing again

    if map_value < 60:
        return 15  # Give Fluids for low MAP
    if resp_rate < 8:
        return 29  # Use Bag Valve Mask
    if sats < 88:
        return 30  # Use NonRebreather Mask

    if all([resp_rate >= 8, map_value >= 60, sats >= 88]):
        return 48  # Finish if vitals are stable

    return 1  # Check signs of life

global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
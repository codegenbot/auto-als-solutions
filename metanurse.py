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

    # Initial ABCDE Assessment steps
    if step == 1:
        return 3  # Examine Airway
    if step == 2:
        return 4  # Examine Breathing
    if step == 3:
        return 25  # Use Sats Probe
    if step == 4:
        return 27  # Use BP Cuff
    if step == 5:
        return 16  # View Monitor

    # Emergency response if critical conditions are met
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # Start Chest Compressions if necessary

    # Continuous monitoring and stabilization actions
    if resp_rate is None:
        return 4  # Examine Breathing again if no reading
    if map_value is None:
        return 38  # Check Blood Pressure again if no reading
    if sats is None:
        return 25  # Use Sats Probe again if no reading

    if events[3] == 0 and (events[4] > 0 or events[5] > 0 or events[6] > 0):
        return 31  # Use Yankeur Suction Catheter if Airway issues

    if events[3] == 0:
        return 35  # Perform Airway Maneuvers if airway not clear

    if map_value < 60:
        return 15  # Give Fluids for MAP < 60
    if resp_rate < 8:
        return 29  # Use Bag Valve Mask for low respiration
    if sats < 88:
        return 30  # Use NonRebreather Mask for low sats

    if map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return 48  # Finish if all vitals are stable

    return 1  # Check signs of life symbolic action to keep loop active


global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
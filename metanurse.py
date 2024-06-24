import sys


def get_action(observations):
    global step, airway_clear, checked_breathing, sats_probe_used, bp_cuff_used

    step += 1
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    # Initial Assessments: ABCDE Protocol
    if step == 1:
        return 3  # Examine Airway
    if step == 2:
        return 4  # Examine Breathing
    if step == 3:
        return 27  # Use BP Cuff
    if step == 4:
        return 25  # Use Sats Probe
    if step == 5:
        return 16  # View Monitor

    # Action Plan based on observations
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # Start Chest Compressions if in cardiac arrest

    if not airway_clear or (
        step % 10 == 0 and not checked_breathing
    ):  # Reassess Airway or check periodically
        airway_clear = False
        checked_breathing = False
        sats_probe_used = bp_cuff_used = False
        return 3  # Examine Airway

    if resp_rate is None:
        checked_breathing = True
        return 4  # Examine Breathing
    if map_value is None:
        bp_cuff_used = True
        return 38  # Check Blood Pressure
    if sats is None:
        sats_probe_used = True
        return 25  # Use Sats Probe

    if map_value < 60:
        return 15  # Give Fluids for MAP < 60
    if resp_rate < 8:
        return 29  # Use Bag Valve Mask for respiration
    if sats < 88:
        return 30  # Use NonRebreather Mask for sats < 88

    if map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return 48  # Finish if all vitals are stable

    return 1  # Default action to check signs of life


global step, airway_clear, checked_breathing, sats_probe_used, bp_cuff_used
step = 0
airway_clear = False
checked_breathing = False
sats_probe_used = False
bp_cuff_used = False

for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break
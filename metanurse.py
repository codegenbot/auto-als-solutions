import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    required_measurements = {25, 27, 16, 3}  # SATs Probe, BP Cuff, Monitor, Examine Airway

    def need_measurements():
        return not required_measurements.issubset(actions_taken)

    def need_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action
    
    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        if need_measurements():
            take_action(need_measurement_action())
            continue

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # A - Airway
        if any(events[i] > 0 for i in [4, 5, 6]):  # Airway events
            if events[5] > 0 or events[4] > 0:
                take_action(31)  # Use Yankeur Suction Catheter
            else:
                take_action(36 if events[6] > 0 else 32)  # Perform Head-Tilt Chin-Lift or Use Guedel Airway
            continue

        # B - Breathing
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        # C - Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # Start Chest Compression (CPR)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if any(events[i] > 0 for i in range(28, 33)):  # HeartRhythm events
                take_action(28)  # Attach Defibrillator Pads
                take_action(2)   # Check Rhythm
                take_action(40)  # Charge Defibrillator
                take_action(47)  # Sync
                take_action(41)  # Defibrillator Current Up
            else:
                take_action(15)  # Give Fluids
            continue

        # Early finish condition if all vitals are stable
        if all(vitals[key] is not None and min_value <= vitals[key] <= max_value for key, min_value, max_value in [
                ("Sats", 88, 100), ("RespRate", 8, 20), ("MAP", 60, 100)]):
            take_action(48)  # Finish
            continue

        take_action(1)  # Restart if unsure, CheckSignsOfLife

if __name__ == "__main__":
    stabilize()
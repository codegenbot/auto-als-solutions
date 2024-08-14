import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {25, 27, 16, 3}  # Use SATs Probe, BP Cuff, View Monitor, Examine Airway

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def has_tachyarrhythmia():
        arrhythmia_events = [28, 30, 33, 34, 35, 36, 37, 38]
        return any(events[i] > 0 for i in arrhythmia_events)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if step % 5 == 0:
            take_action(16)  # View Monitor to recheck vitals
            continue

        # Critical condition handling
        if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(23)  # Resume CPR
            continue

        # Low MAP handling
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if has_tachyarrhythmia():
                take_action(24)  # Use Monitor Pads
                take_action(10)  # Give Adrenaline
            else:
                take_action(15)  # Give Fluids
            continue

        # Low Sats handling
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        # Low RespRate handling
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        # Breathing issues handling
        if any(events[i] > 0 for i in [4, 5]):
            take_action(31)  # Use Yankeur Suction Catheter
            continue

        if events[6] > 0:
            take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(29)  # Use Bag-Valve Mask
            continue

        if all(vitals.get(key) is not None for key in ["RespRate", "MAP", "Sats"]):
            if vitals["RespRate"] >= 8 and vitals["MAP"] >= 60 and vitals["Sats"] >= 88:
                take_action(48)  # Finish if stable
                break
        else:
            take_action(16)  # View Monitor to recheck vitals

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {25, 27, 24}

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def has_unstable_tachyarrhythmia(events):
        arrhythmia_events = [28, 29, 30, 31, 32, 33, 34, 35, 36]
        return any(events[i] > 0 for i in arrhythmia_events)
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compression
            continue

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if has_unstable_tachyarrhythmia(events):
                if 24 not in actions_taken:
                    take_action(24)  # Use monitor pads
                elif 40 not in actions_taken:
                    take_action(40)  # Defibrillator charge
                elif 47 not in actions_taken:
                    take_action(47)  # Defibrillator sync
                else:
                    take_action(48)  # Finish
            else:
                take_action(15)  # Give fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use bag-valve mask
            continue

        if any(events[i] > 0 for i in [4, 5, 6]):  # Examine airway problems
            take_action(3)  # Examine airway
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):  # Examine breathing
            take_action(4)  # Examine breathing
            continue

        if any(events[i] > 0 for i in range(1, 4)):  # Examine response
            take_action(8)  # Examine response
            continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
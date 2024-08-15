import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
    
    def needs_measurements():
        required_measurements = {25, 27, 24}
        return not required_measurements <= actions_taken

    def next_measurement_action():
        for action in {25, 27, 24}:
            if action not in actions_taken:
                return action

    def has_unstable_tachyarrhythmia(events):
        tachyarrhythmia_events = [31, 32, 33, 34, 35, 36, 37, 38, 39]
        return any(events[i] > 0 for i in tachyarrhythmia_events)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        measurements = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (measurements["MAP"] is not None and measurements["MAP"] < 20) or (
            measurements["Sats"] is not None and measurements["Sats"] < 65
        ):
            take_action(17)  # Start chest compression
            continue

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if measurements["MAP"] is not None and measurements["MAP"] < 60:
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

        if measurements["Sats"] is not None and measurements["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if measurements["RespRate"] is not None and measurements["RespRate"] < 8:
            take_action(29)  # Use bag-valve mask
            continue

        if any(events[i] > 0 for i in [4, 5, 6]):  # Examine airway problems
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Use yankeur suction catheter
            elif events[6] > 0:
                take_action(36)  # Perform head-tilt chin-lift
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):  # Examine breathing
            if events[7] > 0:
                take_action(29)  # Use bag-valve mask
            if events[13] > 0:
                take_action(5)   # Perform needle decompression
            continue

        if any(events[i] > 0 for i in range(1, 4)):  # Examine response
            take_action(8)  # Examine response
            continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
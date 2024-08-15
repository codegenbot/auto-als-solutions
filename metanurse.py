import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    initial_measurements = [24, 25, 27, 26]

    def next_initial_measurement_action():
        for action in initial_measurements:
            if action not in actions_taken:
                return action

    def needs_initial_measurements():
        return not all(action in actions_taken for action in initial_measurements)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compression
            take_action(23)  # Resume CPR
            continue

        if needs_initial_measurements():
            take_action(next_initial_measurement_action())
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(40)  # DefibrillatorCharge
            take_action(41)  # DefibrillatorCurrentUp
            take_action(47)  # DefibrillatorSync
            take_action(43)  # DefibrillatorPace
            continue

        if all(v is not None and vitals[v] >= thresholds for v, thresholds in {
            "MAP": 60,
            "Sats": 88,
            "RR": 8,
        }.items()):
            take_action(48)  # Finish
            break
        
        take_action(0)  # DoNothing

if __name__ == "__main__":
    stabilize()
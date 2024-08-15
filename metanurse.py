import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    def get_measurements():
        for action in [25, 26, 27, 28]:
            if action not in actions_taken:
                return action
        return None

    for step in range(max_steps):
        observations = list(map(float, sys.stdin.readline().strip().split()))
        if len(observations) != 53:
            continue

        events, vitals_times, vitals_values = observations[:33], observations[33:40], observations[40:]
        vitals = {
            "HR": vitals_values[0] if vitals_times[0] > 0 else None,
            "RR": vitals_values[1] if vitals_times[1] > 0 else None,
            "MAP": vitals_values[4] if vitals_times[4] > 0 else None,
            "Sats": vitals_values[5] if vitals_times[5] > 0 else None,
        }

        # Airway examination
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            if events[6] > 0:
                take_action(32)
            continue

        # Ensure vital sign measurements
        measurement_action = get_measurements()
        if measurement_action:
            take_action(measurement_action)
            continue

        # Check for critical conditions and address them
        if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(17)  # Start chest compressions
            break

        # Address oxygen saturation if below 88%
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        # Address respiration rate if below 8
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask
            continue

        # Examine breathing if necessary
        if any(events[i] > 0 for i in range(7, 14)):
            take_action(4)  # Examine breathing
            continue

        # Maintain minimum MAP level
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        # Examine circulation if needed
        if any(events[i] > 0 for i in range(14, 21)):
            take_action(5)  # Examine circulation
            continue

        # Finish if step limit reached
        if step >= 349:
            take_action(48)
            break

        take_action(0)  # Do nothing

if __name__ == "__main__":
    stabilize()
import sys


def stabilize():
    max_steps = 350
    steps_taken = 0
    actions_taken = set()

    def take_action(action):
        nonlocal steps_taken
        print(action)
        actions_taken.add(action)
        steps_taken += 1

    initial_measurements = [24, 25, 27, 26]

    def needs_initial_measurements():
        return not all(action in actions_taken for action in initial_measurements)

    def next_initial_measurement_action():
        for action in initial_measurements:
            if action not in actions_taken:
                return action

    while steps_taken < max_steps:
        observations = list(map(float, sys.stdin.readline().strip().split()))
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

        # Cardiac arrest check
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compression
            take_action(23)  # Resume CPR
            continue

        # Initial measurements
        if needs_initial_measurements():
            take_action(next_initial_measurement_action())
            continue

        # ABCDE assessment and stabilization
        if any(events[i] > 0 for i in range(3, 7)):  # Airway issues
            take_action(3)  # Examine Airway
            if events[5] > 0:
                take_action(31)  # Use Yankeur Suction
            if events[6] > 0:
                take_action(32)  # Use Guedel Airway
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:  # Low oxygen saturation
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:  # Low respiratory rate
            take_action(29)  # Use Bag Valve Mask
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing issues
            take_action(4)  # Examine Breathing
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:  # Low MAP
            take_action(15)  # Give fluids
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation issues
            take_action(5)  # Examine Circulation
            continue

        if any(events[i] > 0 for i in range(20, 26)):  # Disability issues
            take_action(6)  # Examine Disability
            continue

        if any(events[i] > 0 for i in range(26, 33)):  # Exposure issues
            take_action(7)  # Examine Exposure
            continue

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()
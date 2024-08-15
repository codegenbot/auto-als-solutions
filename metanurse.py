import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()  # Ensure the action is output immediately

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
            observations[40:]
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

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # Examine airway
            if events[5] > 0:  # AirwayBlood
                take_action(31)  # Use Yankeur suction catheter
            if events[6] > 0:  # AirwayTongue
                take_action(32)  # Use Guedel airway
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # Examine breathing
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # Examine circulation
            if events[17] > 0:  # RadialPulseNonPalpable
                take_action(22)  # Bag during CPR
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # Examine disability
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # Examine exposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
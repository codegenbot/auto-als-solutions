import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    essential_measurements = [24, 25, 27, 26]

    def next_essential_measurement_action():
        for action in essential_measurements:
            if action not in actions_taken:
                return action

    def needs_essential_measurements():
        return not all(action in actions_taken for action in essential_measurements)

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
            take_action(17)
            continue

        if needs_essential_measurements():
            take_action(next_essential_measurement_action())
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # Examine Airway
            if events[5] > 0:
                take_action(31)  # Suction with Yankeur
            if events[6] > 0:
                take_action(32)  # Insert Guedel Airway
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # Examine Breathing
            if vitals["Sats"] is not None and vitals["Sats"] < 88:
                take_action(30)  # Use Non-Rebreather Mask
            if vitals["RR"] is not None and vitals["RR"] < 8:
                take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # Examine Circulation
            if vitals["HR"] is not None and vitals["HR"] > 150:
                take_action(40)  # Defibrillator Charge
                take_action(47)  # Defibrillator Sync
                take_action(43)  # Defibrillator Pace
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # Examine Disability
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # Examine Exposure
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
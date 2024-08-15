import sys

def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)
        sys.stdout.flush()

    required_measurements = [24, 25, 27]  # MonitorPads, SatsProbe, BP Cuff
    actions_taken = set()

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

        # Emergency check: Cardiac arrest
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # Start chest compression immediately
            continue

        # Ensure all required measurements are taken
        if not all(action in actions_taken for action in required_measurements):
            for action in required_measurements:
                if action not in actions_taken:
                    take_action(action)
                    actions_taken.add(action)
                    break
            continue

        # Check ABCDE and perform actions
        # A - Airway
        if events[3] <= 0:  # Airway hasn't been examined
            take_action(3)
            continue
        if any(events[i] > 0 for i in range(4, 7)):  # Check for obstruction
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Use suction
                continue
            elif events[6] > 0:
                take_action(32)  # Use Guedel airway
                continue

        # B - Breathing
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag-valve mask
            continue
        if events[7] <= 0:  # Breathing hasn't been examined
            take_action(4)
            continue

        # C - Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Administer fluids
            continue
        if events[5] <= 0:  # Circulation hasn't been examined
            take_action(5)
            continue

        # D - Disability
        if events[21] <= 0:  # Disability hasn't been examined
            take_action(6)
            continue

        # E - Exposure
        if events[27] <= 0:  # Exposure hasn't been examined
            take_action(7)
            continue

        take_action(48)  # Finish action
        break

if __name__ == "__main__":
    stabilize()
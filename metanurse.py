import sys

def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)

    required_measurements = [24, 25, 27]  # MonitorPads, SatsProbe, BP Cuff
    actions_taken = set()

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

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # Start chest compression immediately
            continue

        if not all(action in actions_taken for action in required_measurements):
            for action in required_measurements:
                if action not in actions_taken:
                    take_action(action)
                    actions_taken.add(action)
                    break
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing assessment
            take_action(4)
            continue
        
        if any(events[i] > 0 for i in range(3, 7)):  # Airway assessment
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Suction
            elif events[6] > 0:
                take_action(32)  # Guedel airway
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag-valve mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Administer fluids
            continue

        take_action(48)  # Finish action
        break

if __name__ == "__main__":
    stabilize()
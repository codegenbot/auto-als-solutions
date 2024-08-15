import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [24, 25, 27]  # MonitorPads, SatsProbe, BP Cuff

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not all(action in actions_taken for action in required_measurements)

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

        # Immediate checks for critical conditions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # Start chest compression immediately
            continue

        # Ensure all required measurements are taken
        if needs_measurements():
            take_action(next_measurement_action())
            continue

        # Handle Airway problems
        if any(events[i] > 0 for i in range(3, 7)):  # Airway assessment
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Use suction catheter for vomit or blood
            elif events[6] > 0:
                take_action(32)  # Use guedel airway for tongue obstruction
            continue
        
        # Check and handle breathing issues
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag-valve mask
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing assessment
            take_action(4)
            continue

        # Check and handle circulation issues
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Administer fluids to raise MAP
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation assessment
            take_action(5)
            continue

        # Check rhythm and tachyarrhythmia
        if vitals["HR"] is not None and any(events[i] > 0 for i in range(27, 40)):  # Abnormal heart rhythms
            take_action(24)  # Use defib pads
            take_action(2)   # Check rhythm
            continue

        take_action(48)  # Finish action
        break

if __name__ == "__main__":
    stabilize()
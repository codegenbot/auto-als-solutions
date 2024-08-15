import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    required_measurements = {24, 25, 27, 16}

    def take_action(action):
        print(action)
        actions_taken.add(action)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    for step in range(max_steps):
        observations = list(map(float, sys.stdin.readline().strip().split()))
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

        # Handle cardiac arrest conditions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compression
            continue
        
        # Ensure all measurements are taken
        if needs_measurements():
            take_action(next_measurement_action())
            continue
        
        # Airway examination and clearing
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Use Yankeur suction catheter for vomit/blood
            elif events[6] > 0:
                take_action(32)  # Use Guedel airway for tongue obstruction
            continue

        # Breathing examination and oxygen management
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue
        
        # Circulation examination and fluid therapy
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue
        
        # Cardiac rhythm management
        if events[28] > 0 or events[29] > 0:  # Check unstable rhythms like VT or SVT
            take_action(28)  # Attach defib pads
            take_action(40)  # Charge the defibrillator
            take_action(41)  # Increase Defibrillator current
            take_action(43)  # Start pacing if needed
            continue

        # Regular checks every 5 and 10 steps
        if step % 5 == 0:
            take_action(1)

        if step % 10 == 0:
            take_action(2)

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
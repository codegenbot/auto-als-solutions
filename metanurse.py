import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [24, 25, 27]

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

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compressions
            continue

        if needs_measurements():
            next_action = next((a for a in required_measurements if a not in actions_taken), None)
            if next_action:
                take_action(next_action)
            continue

        if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
            take_action(3)  # Examine airway
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Use suction catheter
            elif events[6] > 0:
                take_action(32)  # Use Guedel airway
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask
            continue
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # Examine breathing
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # Examine circulation
            continue

        tachyarrhythmia_events = {28, 30, 31, 32, 34, 35}
        if any(events[i] > 0 for i in tachyarrhythmia_events):
            take_action(24)  # Use monitor pads
            take_action(43)  # Defibrillator pace
            continue

        if any(events[i] > 0 for i in range(20, 27)):
            take_action(6)  # Examine disability
            continue
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # Examine circulation
            continue

        take_action(48)  # Finish scenario
        break

if __name__ == "__main__":
    stabilize()
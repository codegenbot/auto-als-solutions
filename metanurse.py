import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    attached_devices = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        attached_devices.add(action)
        sys.stdout.flush()

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

        # Check for cardiac arrest condition first
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compression immediately
            continue

        # Attach necessary devices first
        required_devices = [24, 25, 27]
        for device in required_devices:
            if device not in attached_devices:
                take_action(device)
                continue

        # Perform A - Airway assessment
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Use suction catheter for vomit or blood
            elif events[6] > 0:
                take_action(32)  # Use airway if tongue obstruction
            continue

        # Perform B - Breathing assessment and treatment
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
        elif vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag-valve mask
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue

        # Perform C - Circulation assessment and treatment
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Administer fluids to raise MAP
        if any(events[27+i] > 0 for i in range(9)):
            take_action(24)  # Use defibrillator pads
            take_action(43)  # Defibrillator pace (cardioversion)
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue

        # Perform D - Disability assessment
        if any(events[21 + i] > 0 for i in range(4)):
            take_action(6)
            continue

        # Perform E - Exposure assessment
        if any(events[25 + i] > 0 for i in range(3)):
            take_action(7)
            continue

        # Finish Assessment
        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
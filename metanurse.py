import sys

def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

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

        if not any(events[3:7]):
            take_action(3)  # Examine airway
            continue
        elif events[4] > 0:
            take_action(31)  # Use suction catheter
            continue
        elif events[6] > 0:
            take_action(32)  # Use guedel airway
            continue

        if not any([vitals["Sats"], vitals["RR"], vitals["MAP"]]):
            for action in [27, 25, 38]:  # Attach BP cuff, Use Sats probe, Check BP
                if action not in actions_taken:
                    take_action(action)
                    actions_taken.add(action)
                    break
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag-valve mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if vitals["HR"] is not None and (vitals["HR"] < 60 or vitals["HR"] > 100):
            take_action(24)  # Examine monitor
            take_action(43)  # Use defibrillator pace
            continue
        
        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
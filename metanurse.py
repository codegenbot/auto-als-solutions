import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined, current_action_idx = 350, set(), 0
    actions = [16, 25, 27]

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue
        
        events = observations[:33]
        recent_measurements = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if recent_measurements[0] > 0 else None,
            "RR": measurements[1] if recent_measurements[1] > 0 else None,
            "Glucose": measurements[2] if recent_measurements[2] > 0 else None,
            "Temp": measurements[3] if recent_measurements[3] > 0 else None,
            "MAP": measurements[4] if recent_measurements[4] > 0 else None,
            "Sats": measurements[5] if recent_measurements[5] > 0 else None,
            "Resps": measurements[6] if recent_measurements[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if (vitals["Sats"] and vitals["Sats"] < 88) or not vitals["Sats"]:
            take_action(30)
            continue

        if (vitals["MAP"] and vitals["MAP"] < 60) or not vitals["MAP"]:
            take_action(15)
            continue

        if (vitals["RR"] and vitals["RR"] < 8) or not vitals["RR"]:
            take_action(29)
            continue

        if current_action_idx < len(actions):
            take_action(actions[current_action_idx])
            current_action_idx += 1
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        if events[3] and not any(events[7:15]) and "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)
                continue
            elif vitals["HR"] and vitals["HR"] < 50:
                take_action(12)
                continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
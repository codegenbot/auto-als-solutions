import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def get_observations():
        try:
            return list(map(float, input().strip().split()))
        except:
            take_action(48)
            sys.exit()

    actions_taken = set()
    steps = 350

    for _ in range(steps):
        observations = get_observations()
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        measured_recent = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if measured_recent[0] > 0 else None,
            "RR": measurements[1] if measured_recent[1] > 0 else None,
            "Glucose": measurements[2] if measured_recent[2] > 0 else None,
            "Temp": measurements[3] if measured_recent[3] > 0 else None,
            "MAP": measurements[4] if measured_recent[4] > 0 else None,
            "Sats": measurements[5] if measured_recent[5] > 0 else None,
            "Resps": measurements[6] if measured_recent[6] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if "Airway" not in actions_taken:
            take_action(3)
            actions_taken.add("Airway")
            continue

        if not any(events[3:7]):
            take_action(3)
            continue

        if vitals["Sats"] is None:
            take_action(25)
            continue

        if vitals["MAP"] is None:
            take_action(27)
            continue

        if "Breathing" not in actions_taken:
            take_action(4)
            actions_taken.add("Breathing")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if "Circulation" not in actions_taken:
            take_action(5)
            actions_taken.add("Circulation")
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)
                continue
            elif vitals["HR"] < 50:
                take_action(12)
                continue
            elif vitals["HR"] > 100:
                take_action(9)
                continue

        if "Disability" not in actions_taken:
            take_action(6)
            actions_taken.add("Disability")
            continue

        if "Exposure" not in actions_taken:
            take_action(7)
            actions_taken.add("Exposure")
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
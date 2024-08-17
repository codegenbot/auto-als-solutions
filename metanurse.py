import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()
    for step in range(steps):
        try:
            observations = list(map(float, input().strip().split()))
        except:
            take_action(48)
            return
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        vitals = {
            "HR": observations[46] if observations[40] > 0 else None,
            "RR": observations[47] if observations[41] > 0 else None,
            "Glucose": observations[48] if observations[42] > 0 else None,
            "Temp": observations[49] if observations[43] > 0 else None,
            "MAP": observations[50] if observations[44] > 0 else None,
            "Sats": observations[51] if observations[45] > 0 else None,
            "Resps": observations[52] if observations[46] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        if "Sats" not in examined and vitals["Sats"] is None:
            take_action(25)
            examined.add("Sats")
            continue

        if "MAP" not in examined and vitals["MAP"] is None:
            take_action(27)
            examined.add("MAP")
            continue

        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        if "Circulation" not in examined:
            take_action(5)
            examined.add("Circulation")
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

        if vitals["HR"] is not None:
            if vitals["HR"] > 150:
                take_action(24)
                continue
            elif vitals["HR"] < 50:
                take_action(12)
                continue
            elif vitals["HR"] > 100:
                take_action(9)
                continue

        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()
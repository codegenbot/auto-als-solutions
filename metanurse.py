import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] != 0 else None,
            "RR": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if "airway" not in examined:
            take_action(3)
            examined.add("airway")
            continue

        if events[3] > 0:
            examined.add("airway_clear")
        elif events[4] > 0 or events[5] > 0 or events[6] > 0:
            take_action(35)
            continue

        if "Sats" not in examined:
            take_action(25)
            examined.add("Sats")
            continue

        if "RR" not in examined:
            take_action(4)
            examined.add("RR")
            continue

        if "BP" not in examined:
            take_action(27)
            examined.add("BP")
            continue

        if "HR" not in examined:
            take_action(24)
            examined.add("HR")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(20, 26)) and "disability" not in examined:
            take_action(6)
            examined.add("disability")
            continue

        if any(events[i] > 0 for i in range(26, 33)) and "exposure" not in examined:
            take_action(7)
            examined.add("exposure")
            continue

        if vitals["HR"] is not None and (vitals["HR"] < 60 or vitals["HR"] > 150):
            take_action(2)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
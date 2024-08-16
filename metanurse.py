import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
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

        if "airway" not in examined_vitals:
            take_action(3)
            examined_vitals.add("airway")
            continue

        if events[3] > 0:  # AirwayClear
            take_action(8)  # Check response
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)
            examined_vitals.add("Sats")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(4)
            examined_vitals.add("RR")
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)
            examined_vitals.add("MAP")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if "circulation" not in examined_vitals:
            take_action(5)
            examined_vitals.add("circulation")
            continue

        if "disability" not in examined_vitals:
            take_action(6)
            examined_vitals.add("disability")
            continue

        if "exposure" not in examined_vitals:
            take_action(7)
            examined_vitals.add("exposure")
            continue

        if all(v is not None for v in [vitals["Sats"], vitals["RR"], vitals["MAP"]]):
            take_action(48)
            break

        take_action(0)

if __name__ == "__main__":
    stabilize()
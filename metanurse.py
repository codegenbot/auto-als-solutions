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
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30 if 30 not in examined_vitals else 29)
            examined_vitals.add(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if "monitor" not in examined_vitals:
            take_action(16)
            examined_vitals.add("monitor")
            continue

        if vitals["MAP"] is None and "BP" not in examined_vitals:
            take_action(27)
            examined_vitals.add("BP")
            continue

        if vitals["Sats"] is None and "SatsProbe" not in examined_vitals:
            take_action(25)
            examined_vitals.add("SatsProbe")
            continue

        if vitals["RR"] is None and "Breathing" not in examined_vitals:
            take_action(4)
            examined_vitals.add("Breathing")
            continue

        if any(events[i] > 0 for i in range(3, 7)) and "Airway" not in examined_vitals:
            take_action(3)
            examined_vitals.add("Airway")
            continue

        if any(events[28:33]):  # Check for abnormal heart rhythms
            take_action(2)
            continue

        if (
            any(events[i] > 0 for i in range(7, 15))
            and "Breathing" not in examined_vitals
        ):
            take_action(4)
            examined_vitals.add("Breathing")
            continue

        if (
            any(events[i] > 0 for i in range(15, 20))
            and "Circulation" not in examined_vitals
        ):
            take_action(5)
            examined_vitals.add("Circulation")
            continue

        if in_range > 20 and any(events[i] > 0 for i in range(20, 26))and "Disability" not in examined_vitals:
            take_action(6)
            examined_vitals.add("Disability")
            continue

        if (
            any(events[i] > 0 for i in range(26, 33))
            and "Exposure" not in examined_vitals
        ):
            take_action(7)
            examined_vitals.add("Exposure")
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
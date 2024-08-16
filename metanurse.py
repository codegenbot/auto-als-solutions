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

        if not all(key in examined_vitals for key in ["airway", "breathing", "circulation"]):
            if not "airway" in examined_vitals:
                take_action(3)
                examined_vitals.add("airway")
                continue

            if not "breathing" in examined_vitals:
                take_action(4)
                examined_vitals.add("breathing")
                continue

            if not "MAP" in examined_vitals:
                take_action(27)
                examined_vitals.add("MAP")
                continue

            if vitals["HR"] is None and "HR" not in examined_vitals:
                take_action(5)
                examined_vitals.add("HR")
                continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["HR"] is not None:
            if vitals["HR"] > 150:
                take_action(40)
                take_action(41)
                take_action(47)
                take_action(43)
                continue
            elif vitals["HR"] < 60:
                take_action(10)
                continue

        if all(vitals[v] is not None for v in ["Sats", "RR", "MAP"]) and vitals["Sats"] >= 88 and vitals["RR"] >= 8 and vitals["MAP"] >= 60:
            take_action(48)
            break

if __name__ == "__main__":
    stabilize()
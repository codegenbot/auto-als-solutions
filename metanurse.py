import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    used_airway = False

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
            if "MAP" in examined_vitals:
                take_action(15)
            else:
                take_action(27)
                examined_vitals.add("MAP")
            continue

        if vitals["HR"] is not None and vitals["HR"] > 100:
            take_action(24)
            continue
        
        if any(events[i] > 0 for i in range(3, 7)) and not used_airway:
            take_action(3)
            examined_vitals.add("airway")
            continue
        
        if vitals["Sats"] is None:
            if "Sats" not in examined_vitals:
                take_action(25)
                examined_vitals.add("Sats")
            else:
                take_action(16)
            continue
        elif vitals["Sats"] < 88:
            if "mask" not in examined_vitals:
                take_action(30)
                examined_vitals.add("mask")
            else:
                take_action(29)
            continue
        
        if vitals["RR"] is None or vitals["RR"] < 8:
            take_action(4)
            continue

        if any(events[i] > 0 for i in range(20, 26)) and "disability" not in examined_vitals:
            take_action(6)
            examined_vitals.add("disability")
            continue

        if any(events[i] > 0 for i in range(26, 33)) and "exposure" not in examined_vitals:
            take_action(7)
            examined_vitals.add("exposure")
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
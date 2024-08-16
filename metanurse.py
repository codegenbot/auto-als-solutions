import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    
    def measure_and_treat_vitals():
        actions = [
            (25, "SatsProbe"),
            (4, "RespRate"),
            (27, "BP"),
            (38, "CheckBP"),
            (16, "Monitor"),
        ]
        for action, item in actions:
            if item not in examined:
                take_action(action)
                examined.add(item)
                return

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if "airway" not in examined:
            take_action(3)
            examined.add("airway")
            continue

        if events[3] > 0:
            examined.add("AirwayClear")

        measure_and_treat_vitals()

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if events[29] > 0 or events[30] > 0 or (vitals["HR"] is not None and (vitals["HR"] < 50 or vitals["HR"] > 150)):
            take_action(28)
            take_action(40)
            take_action(41)
            take_action(43)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
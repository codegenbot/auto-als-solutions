import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    step = 0
    examined = set()
    vitals_checklist = ["Monitor", "SatsProbe", "BP"]

    while step < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            step += 1
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "Glucose": values[2] if times[2] > 0 else None,
            "Temp": values[3] if times[3] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
            "Resps": values[6] if times[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)
            step += 1
            continue

        if "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            step += 1
            continue

        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            step += 1
            continue

        for check in vitals_checklist:
            if check not in examined:
                if check == "Monitor":
                    take_action(16)
                elif check == "SatsProbe":
                    take_action(25)
                elif check == "BP":
                    take_action(27)
                examined.add(check)
                step += 1
                continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            step += 1
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            step += 1
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            step += 1
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150 or vitals["HR"] < 50:
                take_action(2)
                step += 1
                continue

        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()
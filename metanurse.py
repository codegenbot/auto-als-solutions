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

        vitals = { "HR": values[0] if times[0] > 0 else None,
                   "RR": values[1] if times[1] > 0 else None,
                   "Glucose": values[2] if times[2] > 0 else None,
                   "Temp": values[3] if times[3] > 0 else None,
                   "MAP": values[4] if times[4] > 0 else None,
                   "Sats": values[5] if times[5] > 0 else None,
                   "Resps": values[6] if times[6] > 0 else None }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if "Airway" not in examined:
            examine = [3]
            if events[4] > 0: examine.append(31)
            if events[5] > 0 or events[6] > 0: examine.append(35)
            examined.add("Airway")
            for action in examine:
                take_action(action)
            continue

        if "Breathing" not in examined:
            actions = [4]
            if vitals["Sats"] and vitals["Sats"] < 88: actions.append(30)
            examined.add("Breathing")
            for action in actions:
                take_action(action)
            continue

        if "Circulation" not in examined:
            actions = [5, 27, 38]
            if vitals["MAP"] and vitals["MAP"] < 60: actions.append(15)
            if vitals["HR"] and (vitals["HR"] < 50 or vitals["HR"] > 150): actions.append(28)
            examined.add("Circulation")
            for action in actions:
                take_action(action)
            continue

        if "Disability" not in examined:
            take_action(6)
            examined.add("Disability")
            continue

        if "Exposure" not in examined:
            take_action(7)
            examined.add("Exposure")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
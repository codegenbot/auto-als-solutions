import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def examine_vitals():
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
            return
        if "BP" not in examined:
            take_action(27)
            examined.add("BP")
            return
        if "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
            return
        if "RespRate" not in examined:
            take_action(4)
            examined.add("RespRate")
            return

    examined = set()
    checked_prerequisites = False

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = dict()
        vitals["HR"] = values[0] if times[0] > 0 else None
        vitals["RR"] = values[1] if times[1] > 0 else None
        vitals["MAP"] = values[4] if times[4] > 0 else None
        vitals["Sats"] = values[5] if times[5] > 0 else None

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if not checked_prerequisites:
            if events[3] == 0:
                take_action(3)
                continue
            if events[7] == 0:
                take_action(4)
                continue
            if events[16] == 0:
                take_action(5)
                continue
            checked_prerequisites = True

        examine_vitals()

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["HR"] and (vitals["HR"] > 150):
            take_action(28)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def measure_vitals():
        for check in ["Monitor", "BP", "SatsProbe", "RespRate"]:
            if check not in examined:
                action_map = {"Monitor": 16, "BP": 27, "SatsProbe": 25, "RespRate": 4}
                take_action(action_map[check])
                examined.add(check)
                return

    examined = set()

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
        vitals["Glucose"] = values[2] if times[2] > 0 else None
        vitals["Temp"] = values[3] if times[3] > 0 else None
        vitals["MAP"] = values[4] if times[4] > 0 else None
        vitals["Sats"] = values[5] if times[5] > 0 else None
        vitals["Resps"] = values[6] if times[6] > 0 else None

        # Immediate action if critical vitals
        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        # Airway assessment
        if events[3] == 0 and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        # Breathing assessment
        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        # Circulation assessment
        if "Circulation" not in examined:
            take_action(5)
            examined.add("Circulation")
            continue

        # Perform measures for stabilization
        measure_vitals()

        # Check vitals and stabilize
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        if (
            events[29] > 0
            or events[30] > 0
            or (vitals["HR"] and (vitals["HR"] < 50 or vitals["HR"] > 150))
        ):
            take_action(28)
            continue

        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()
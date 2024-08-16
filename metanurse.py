import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def examine_vitals():
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
            return
        if "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
            return
        if "BP" not in examined:
            take_action(27)
            examined.add("BP")
            return

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if observations[33] > 0 else None,
            "RR": values[1] if observations[34] > 0 else None,
            "Glucose": values[2] if observations[35] > 0 else None,
            "Temp": values[3] if observations[36] > 0 else None,
            "MAP": values[4] if observations[37] > 0 else None,
            "Sats": values[5] if observations[38] > 0 else None,
            "Resps": values[6] if observations[39] > 0 else None,
        }

        # Start with airway assessment
        if "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        if events[3] > 0:  # AirwayClear
            # Proceed to Breathing
            if "Breathing" not in examined:
                take_action(4)
                examined.add("Breathing")
                continue

            examine_vitals()

            if (
                vitals["Sats"]
                and vitals["Sats"] < 65
                or vitals["MAP"]
                and vitals["MAP"] < 20
            ):
                take_action(17)
                continue

            if vitals["Sats"] and vitals["Sats"] < 88:
                take_action(30)
                continue

            if vitals["RR"] and vitals["RR"] < 8:
                take_action(29)
                continue

        if events[7] > 0:  # BreathingNone
            take_action(29)
            continue

        # Proceed to Circulation
        if "Circulation" not in examined:
            take_action(5)
            examined.add("Circulation")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)
                continue
            elif vitals["HR"] > 100:
                take_action(9)
                continue
            elif vitals["HR"] < 50:
                take_action(12)
                continue

        # Disability and Exposure assessments
        if "Disability" not in examined:
            take_action(6)
            examined.add("Disability")
            continue

        if "Exposure" not in examined:
            take_action(7)
            examined.add("Exposure")
            continue

        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()
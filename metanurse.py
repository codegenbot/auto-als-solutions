import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def measure_all_vitals():
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
        elif "BP" not in examined:
            take_action(27)
            examined.add("BP")
        elif "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
        elif "RespRate" not in examined:
            take_action(4)
            examined.add("RespRate")

    def administer_fluids():
        take_action(15)

    def perform_cardioversion():
        take_action(40)  # DefibrillatorCharge
        take_action(41)  # DefibrillatorCurrentUp
        take_action(43)  # DefibrillatorPace

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

        if events[3] > 0:
            examined.add("airway")

        if "airway" not in examined:
            take_action(3)
            continue

        measure_all_vitals()

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            administer_fluids()
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["HR"] is not None and (vitals["HR"] < 50 or vitals["HR"] > 150):
            perform_cardioversion()
            continue

        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()
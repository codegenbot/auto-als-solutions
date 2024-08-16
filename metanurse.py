import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def examine_airway():
        if "airway" not in examined:
            take_action(3)
            examined.add("airway")
            return True
        return False

    def examine_breathing():
        if "breathing" not in examined:
            take_action(4)
            examined.add("breathing")
            return True
        return False

    def examine_circulation():
        if "circulation" not in examined:
            take_action(5)
            examined.add("circulation")
            return True
        return False

    def measure_all_vitals():
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
            return True
        elif "BP" not in examined:
            take_action(27)
            examined.add("BP")
            return True
        elif "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
            return True
        elif "RespRate" not in examined:
            take_action(4)
            examined.add("RespRate")
            return True
        return False

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
            take_action(17)  # Cardiac arrest, start CPR
            continue

        if examine_airway():
            continue

        if events[3] > 0:  # AirwayClear
            examined.add("airway")

        if measure_all_vitals():
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if examine_breathing() or examine_circulation():
            continue

        if any([events[28], events[29], events[30], events[31], events[32]]):
            take_action(40)  # Prepare for defibrillation
            take_action(41)
            take_action(43)

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish


if __name__ == "__main__":
    stabilize()
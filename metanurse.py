import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
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

        # Immediate cardiac arrest procedures
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        # Airway assessment and intervention
        if "airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("airway")
            continue

        if events[3] > 0:
            examined.add("airway")

        # Breathing assessment and intervention
        if "breathing" not in examined:
            take_action(4)  # ExamineBreathing
            examined.add("breathing")
            continue

        if vitals["Sats"] is None:
            take_action(25)  # UseSatsProbe
            continue

        if vitals["RR"] is None:
            take_action(4)  # ExamineBreathing again to measure RR
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Circulation assessment and intervention
        if "circulation" not in examined:
            take_action(27)  # UseBloodPressureCuff
            examined.add("circulation")
            continue

        if vitals["MAP"] is None:
            take_action(27)  # UseBloodPressureCuff for MAP
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Disability and Exposure can be assessed but are less critical for stabilization
        # Checking ending criteria to decide Finish action
        if (
            "airway" in examined
            and "breathing" in examined
            and "circulation" in examined
        ):
            take_action(48)  # Finish
            break

    else:
        take_action(48)  # Finish at the end if not broken out


if __name__ == "__main__":
    stabilize()
import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
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
            take_action(17)  # Start chest compressions
            continue

        airway_events = [3, 4, 5, 6]
        if (
            any(events[i] > 0 for i in airway_events)
            and "airway" not in examined_vitals
        ):
            take_action(3)  # Examine airway
            examined_vitals.add("airway")
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # UseSatsProbe
            examined_vitals.add("Sats")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(4)  # ExamineBreathing
            examined_vitals.add("RR")
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        circulation_events = [16, 17, 18, 19]
        if (
            any(events[i] > 0 for i in circulation_events)
            and "circulation" not in examined_vitals
        ):
            take_action(5)  # ExamineCirculation
            examined_vitals.add("circulation")
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)  # UseBloodPressureCuff
            examined_vitals.add("MAP")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        disability_events = [20, 21, 22, 23, 24]
        if (
            any(events[i] > 0 for i in disability_events)
            and "disability" not in examined_vitals
        ):
            take_action(6)  # ExamineDisability
            examined_vitals.add("disability")
            continue

        exposure_events = [25, 26, 27]
        if any(events[i] > 0 for i in exposure_events):
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()
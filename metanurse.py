import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
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
            take_action(17)  # Start chest compression if vital signs are critical
            continue

        if vitals["MAP"] is None or vitals["Sats"] is None:
            if vitals["MAP"] is None:
                take_action(27)  # UseBloodPressureCuff
            elif vitals["Sats"] is None:
                take_action(25)  # UseSatsProbe
            continue

        if vitals["MAP"] < 60:
            take_action(15)  # GiveFluids to stabilize MAP
            continue

        if vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in range(3, 7)):  # Airway related events
            take_action(3)  # ExamineAirway
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing related events
            take_action(4)  # ExamineBreathing
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation related events
            take_action(5)  # ExamineCirculation
            continue

        if any(events[i] > 0 for i in range(20, 26)):  # Disability related events
            take_action(6)  # ExamineDisability
            continue

        if any(events[i] > 0 for i in range(26, 33)):  # Exposure related events
            take_action(7)  # ExamineExposure
            continue

        take_action(48)
        break


if __name__ == "__main__":
    stabilize()
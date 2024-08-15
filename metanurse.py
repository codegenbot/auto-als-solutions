import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    critical_checks = [27, 25, 38, 16]  # Attach BP cuff, Sats probe, Take BP, View Monitor
    airway_checks = [3, 18, 31, 32, 35, 36, 37]  # ExamineAirway and airway tools/actions
    breathing_checks = [4, 19, 29, 30]  # ExamineBreathing and breathing tools/actions
    circulation_checks = [5, 20, 6, 14, 15]  # ExamineCirculation and circulation tools/actions
    disability_checks = [6, 21, 34]  # ExamineDisability and check glucose
    exposure_checks = [7]  # ExamineExposure

    actions_taken = set()
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
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if vitals["MAP"] is None and 27 not in actions_taken:
            actions_taken.add(27)
            take_action(27)
            continue

        if vitals["Sats"] is None and 25 not in actions_taken:
            actions_taken.add(25)
            take_action(25)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        for check in critical_checks:
            if check not in actions_taken:
                actions_taken.add(check)
                take_action(check)
                break
        else:
            for event_check in airway_checks:
                if any(events[i] > 0 for i in range(3, 7)):
                    take_action(event_check)
                    break
            for event_check in breathing_checks:
                if any(events[i] > 0 for i in range(7, 15)):
                    take_action(event_check)
                    break
            for event_check in circulation_checks:
                if any(events[i] > 0 for i in range(15, 20)):
                    take_action(event_check)
                    break
            for event_check in disability_checks:
                if any(events[i] > 0 for i in range(20, 26)):
                    take_action(event_check)
                    break
            for event_check in exposure_checks:
                if any(events[i] > 0 for i in range(26, 33)):
                    take_action(event_check)
                    break

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
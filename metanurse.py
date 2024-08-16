import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    examined_vitals = set()

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start chest compression in case of cardiac arrest
            continue

        if vitals["MAP"] is None and 27 not in examined_vitals:
            take_action(27)  # UseBloodPressureCuff to measure MAP
            examined_vitals.add(27)
            continue

        if vitals["Sats"] is None and 25 not in examined_vitals:
            take_action(25)  # UseSatsProbe to measure oxygen saturation
            examined_vitals.add(25)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids if MAP is low
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 30 not in actions_taken:
                take_action(30)  # UseNonRebreatherMask if sats are below 88%
                actions_taken.add(30)
                continue
            take_action(29)  # UseBagValveMask if oxygen saturation is critical
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask if respiratory rate is below 8
            continue

        if any(events[i] > 0 for i in range(3, 7)) and 3 not in actions_taken:
            take_action(3)  # ExamineAirway if any airway-related event occurred
            actions_taken.add(3)
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # ExamineBreathing if any breathing-related event occurred
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # ExamineCirculation if any circulation-related event occurred
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # ExamineDisability if any disability-related event occurred
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # ExamineExposure if any exposure-related event occurred
            continue

        take_action(48)  # Finish the assessment
        break

if __name__ == "__main__":
    stabilize()
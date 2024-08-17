import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps = 350
    actions_taken = set()

    for step in range(steps):
        observations = list(map(float, input().strip().split()))

        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        timestamps = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if timestamps[0] > 0 else None,
            "RR": measurements[1] if timestamps[1] > 0 else None,
            "Glucose": measurements[2] if timestamps[2] > 0 else None,
            "Temp": measurements[3] if timestamps[3] > 0 else None,
            "MAP": measurements[4] if timestamps[4] > 0 else None,
            "Sats": measurements[5] if timestamps[5] > 0 else None,
            "Resps": measurements[6] if timestamps[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if "ExamineAirway" not in actions_taken:
            take_action(3)
            actions_taken.add("ExamineAirway")
            continue

        if any(events[3:7]):
            if events[5] or events[4]:
                take_action(31)
                continue
            elif events[6]:
                take_action(35)
                continue

        if "ExamineBreathing" not in actions_taken:
            take_action(4)
            actions_taken.add("ExamineBreathing")
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        if "ViewMonitor" not in actions_taken:
            take_action(16)
            actions_taken.add("ViewMonitor")
            continue

        if "UseSatsProbe" not in actions_taken:
            take_action(25)
            actions_taken.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in actions_taken:
            take_action(27)
            actions_taken.add("UseBloodPressureCuff")
            continue

        if "ExamineCirculation" not in actions_taken:
            take_action(5)
            actions_taken.add("ExamineCirculation")
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

        if "ExamineDisability" not in actions_taken:
            take_action(6)
            actions_taken.add("ExamineDisability")
            continue

        if "ExamineExposure" not in actions_taken:
            take_action(7)
            actions_taken.add("ExamineExposure")
            continue

        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()
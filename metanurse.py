import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions = 0
    examined = set()
    need_check = {"ExamineAirway": 3, "ExamineBreathing": 4, "ExamineCirculation": 5, "ExamineDisability": 6, "ExamineExposure": 7, "CheckSignsOfLife": 1}

    def examination_cycle():
        for key, action in need_check.items():
            if key not in examined:
                take_action(action)
                examined.add(key)
                return True
        return False

    while actions < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            actions += 1
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "Glucose": values[2] if times[2] > 0 else None,
            "Temp": values[3] if times[3] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
            "Resps": values[6] if times[6] > 0 else None
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            break

        if events[3] == 0:
            take_action(3)
            actions += 1
            continue

        if examination_cycle():
            actions += 1
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            actions += 1
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            actions += 1
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            actions += 1
            continue

        hr = vitals["HR"]
        if hr and (hr < 50 or hr > 150):
            take_action(28)
            actions += 1
            continue

        break

    take_action(48)

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    for _ in range(350):
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if events[4] > 0 or events[5] > 0 or events[6] > 0:
            take_action(31)
            continue

        if vitals["Sats"] is None:
            take_action(25)
            continue
        if vitals["RR"] is None:
            take_action(4)
            continue
        if vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["MAP"] is None:
            take_action(27)
            continue
        if vitals["MAP"] < 60:
            take_action(15)
            continue

        if events[21] == 0:
            take_action(6)
            continue

        if events[26] > 0 or events[27] > 0:
            take_action(7)
            continue

        if vitals["Sats"] >= 88 and vitals["RR"] >= 8 and vitals["MAP"] >= 60:
            take_action(48)
            break
        else:
            take_action(0)
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
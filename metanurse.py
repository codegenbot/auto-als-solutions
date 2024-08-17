import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps = 350

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        values = observations[46:]

        vitals = {
            "HR": values[0] if observations[33] > 0 else None,
            "RR": values[1] if observations[34] > 0 else None,
            "Glucose": values[2] if observations[35] > 0 else None,
            "Temp": values[3] if observations[36] > 0 else None,
            "MAP": values[4] if observations[37] > 0 else None,
            "Sats": values[5] if observations[38] > 0 else None,
            "Resps": values[6] if observations[39] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if not any(events[3:7]):
            take_action(3)
        elif events[7]:
            take_action(29)
        elif events[8]:
            take_action(36)
        elif vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
        elif vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
        elif vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
        else:
            if observations[33] <= 0:
                take_action(16)
            elif observations[38] <= 0:
                take_action(25)
            elif observations[39] <= 0:
                take_action(27)
            else:
                take_action(48)
                break

if __name__ == "__main__":
    stabilize()
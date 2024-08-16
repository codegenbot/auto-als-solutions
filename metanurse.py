import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps_taken = 0

    while steps_taken < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            steps_taken += 1
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HeartRate": values[0] if times[0] != 0 else None,
            "RespRate": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            steps_taken += 1
            continue
        
        if events[3] == 0:
            take_action(3)
        elif vitals["Sats"] is None:
            take_action(25)
        elif vitals["MAP"] is None:
            take_action(27)
        elif vitals["RespRate"] is None:
            take_action(4)
        elif vitals["MAP"] < 60:
            take_action(15)
        elif vitals["Sats"] < 88:
            take_action(30)
        elif vitals["RespRate"] < 8:
            take_action(29)
        elif (
            events[29] > 0 or events[30] > 0 or 
            (vitals["HeartRate"] is not None and vitals["HeartRate"] > 150)
        ):
            take_action(28)
            take_action(40)
            take_action(41)
            take_action(43)
        else:
            take_action(48)
            break

        steps_taken += 1

    if steps_taken >= 350:
        take_action(48)

if __name__ == "__main__":
    stabilize()
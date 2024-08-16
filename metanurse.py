import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    first_steps = [27, 25, 4, 2]

    for action in first_steps:
        take_action(action)

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

        # Immediate checks for critical condition
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        # Examination and check vitals
        if times[4] == 0:
            take_action(27)
            continue
        if times[5] == 0:
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

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
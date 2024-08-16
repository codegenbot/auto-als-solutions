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
        
        vital_signs = {
            "HR": values[0] if times[0] != 0 else None,
            "RR": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }

        if (vital_signs["Sats"] is not None and vital_signs["Sats"] < 65) or (vital_signs["MAP"] is not None and vital_signs["MAP"] < 20):
            take_action(17)
            continue

        if not any(events[3:7]):
            take_action(3)
            continue

        if events[2]:
            take_action(8)
            continue

        if vital_signs["Sats"] is None:
            take_action(25)
            continue
        
        if vital_signs["RR"] is None:
            take_action(4)
            continue

        if vital_signs["Sats"] < 88:
            take_action(30)
            continue

        if vital_signs["RR"] and vital_signs["RR"] < 8:
            take_action(29)
            continue

        if vital_signs["MAP"] is None:
            take_action(27)
            continue

        if vital_signs["MAP"] < 60:
            take_action(15)
            continue

        if None in vital_signs.values():
            take_action(24)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
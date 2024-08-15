import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    examine_steps = [3, 4, 5, 6, 7]
    
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
            take_action(17)
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 92:
            if 25 not in actions_taken:
                actions_taken.add(25)
                take_action(25)
            else:
                take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if 27 not in actions_taken:
                actions_taken.add(27)
                take_action(27)
            else:
                take_action(15)
            continue

        for action in examine_steps:
            if action not in actions_taken:
                actions_taken.add(action)
                take_action(action)
                break
        else:
            take_action(48)
            break

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    examined_vitals = set()
    
    def need_examine(event_indices):
        return any(events[i] > 0 for i in event_indices)
    
    def check_vital(vital, idx):
        if vital is None and idx not in examined_vitals:
            take_action(idx)
            examined_vitals.add(idx)
            return True
        return False

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

        if check_vital(vitals["MAP"], 27) or check_vital(vitals["Sats"], 25):
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 30 not in actions_taken:
                take_action(30)
                actions_taken.add(30)
                continue
            take_action(29)
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if need_examine(range(3, 7)) and 3 not in actions_taken:
            take_action(3)
            actions_taken.add(3)
            continue
        if need_examine(range(7, 15)):
            take_action(4)
            continue
        if need_examine(range(15,20)):
            take_action(5)
            continue
        if need_examine(range(20, 26)):
            take_action(6)
            continue
        if need_examine(range(26, 33)):
            take_action(7)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
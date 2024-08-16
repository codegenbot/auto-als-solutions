import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def need_vital_check(vital, action):
        return vital is None and action not in actions_taken

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
            take_action(17)
            continue

        if need_vital_check(vitals["MAP"], 27):
            take_action(27)
            actions_taken.add(27)
            continue
        if need_vital_check(vitals["Sats"], 25):
            take_action(25)
            actions_taken.add(25)
            continue
        if need_vital_check(vitals["RR"], 4):
            take_action(4)
            actions_taken.add(4)
            continue
        if need_vital_check(vitals["HR"], 16):
            take_action(16)
            actions_taken.add(16)
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

        if any(events[3:7]):
            take_action(3)
            continue
        if any(events[7:15]):
            take_action(4)
            continue
        if any(events[15:20]):
            take_action(5)
            continue
        if any(events[20:26]):
            take_action(6)
            continue
        if any(events[26:33]):
            take_action(7)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
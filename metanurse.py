import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if vitals["MAP"] is None:
            take_action(27)
            continue
        if vitals["Sats"] is None:
            take_action(25)
            continue
        if vitals["RR"] is None:
            take_action(4)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 30 not in actions_taken:
                actions_taken.add(30)
                take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        significant_heart_rhythm_events = [27, 28, 29, 30, 31, 32]
        if any(events[i] > 0 for i in significant_heart_rhythm_events):
            take_action(24)
            continue
        
        clear_assessments = [
            ("Examine Airway", 3, range(3, 7)),
            ("Examine Breathing", 4, range(7, 15)),
            ("Examine Circulation", 5, range(15, 20)),
            ("Examine Disability", 6, range(20, 26)),
            ("Examine Exposure", 7, range(26, 33)),
        ]
        
        for name, action, event_range in clear_assessments:
            if any(events[i] > 0 for i in event_range):
                take_action(action)
                continue
        
        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
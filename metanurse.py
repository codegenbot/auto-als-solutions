import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    def take_action(action):
        if action not in actions_taken:
            print(action)
            actions_taken.add(action)
            sys.stdout.flush()
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if 25 not in actions_taken:
            take_action(25)
            continue
        if 27 not in actions_taken:
            take_action(27)
            continue
        if 24 not in actions_taken:
            take_action(24)
            continue
        
        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)
            if events[5] > 0:
                take_action(31)
            elif events[6] > 0:
                take_action(36)
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)
            continue

        if any(events[i] > 0 for i in range(1, 4)):
            take_action(1)
            take_action(2)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)
            if events[7] > 0:
                take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
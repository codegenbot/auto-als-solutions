import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    def take_action(action):
        print(action)
        actions_taken.add(action)
    
    def get_vital_signs(vital_signs_times, vital_signs_values):
        return {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        
        events, vital_signs_times, vital_signs_values = (observations[:33], observations[33:40], observations[40:])
        vitals = get_vital_signs(vital_signs_times, vital_signs_values)

        if (vitals["MAP"] and vitals["MAP"] < 20) or (vitals["Sats"] and vitals["Sats"] < 65):
            take_action(17)
            continue

        if 24 not in actions_taken:
            take_action(24)
            continue
        if 25 not in actions_taken:
            take_action(25)
            continue
        if 27 not in actions_taken:
            take_action(27)
            continue

        if (vitals["Sats"] is not None and vitals["Sats"] < 88) or any(events[4:7]):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            elif events[6] > 0:
                take_action(32)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[7:15]):
            take_action(4)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if any(events[15:20]):
            take_action(5)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
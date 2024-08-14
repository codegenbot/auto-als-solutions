import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False
    last_action = None

    def take_action(action):
        nonlocal done, last_action
        actions_taken.add(action)
        print(action)
        sys.stdout.flush()
        last_action = action
        if action == 48:
            done = True
    
    def initialize_measurements():
        return not all(measured(vital_sign) for vital_sign in {25, 27, 16, 3})

    def measured(vital_sign):
        return vital_sign in actions_taken

    def next_measurement_action():
        for action in [25, 27, 16, 3]:
            if action not in actions_taken:
                return action

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        if initialize_measurements():
            take_action(next_measurement_action())
            continue

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue
        
        if not measured(3) or last_action == 3:
            take_action(3)
            continue
        
        if not measured(4) or last_action == 4:
            take_action(4)
            continue
        
        if not measured(5) or last_action == 5:
            take_action(5)
            continue
        
        if not measured(6) or last_action == 6:
            take_action(6)
            continue
        
        if last_action is not None and last_action < 25:
            take_action(last_action + 1)
            continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
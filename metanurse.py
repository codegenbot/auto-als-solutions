import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if 3 not in actions_taken:
            take_action(3)
            continue
        
        if 4 not in actions_taken:
            take_action(4)
            continue

        if 25 not in actions_taken:
            take_action(25)
            continue
        
        if 27 not in actions_taken:
            take_action(27)
            continue

        if 16 not in actions_taken:
            take_action(16)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
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
        
        if (vitals["Sats"] is not None and vitals["Sats"] >= 88 and 
           vitals["RespRate"] is not None and vitals["RespRate"] >= 8 and 
           vitals["MAP"] is not None and vitals["MAP"] >= 60):
            take_action(48)
            break

        take_action(0)

if __name__ == "__main__":
    stabilize()
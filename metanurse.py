import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    checking_sequence = [25, 27, 16, 3, 4, 5]
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
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        while checking_sequence:
            next_action = checking_sequence[0]
            if next_action not in actions_taken:
                take_action(next_action)
                break
            else:
                checking_sequence.pop(0)
        else:
            vitals = {
                "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
                "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
                "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
                "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
            }

            if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
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

            if events[4] > 0 or events[5] > 0 or events[6] > 0:
                take_action(31)
                continue
            if events[7] > 0 or any(events[i] > 0 for i in [10, 11, 12, 13, 14]):
                take_action(29)
                continue

            if any(events[i] > 0 for i in range(28, 33)):
                if 28 not in actions_taken:
                    take_action(28)
                    continue
                take_action(40)
                continue

            take_action(48)

if __name__ == "__main__":
    stabilize()
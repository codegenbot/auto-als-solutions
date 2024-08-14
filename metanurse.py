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

    required_measurements = [25, 27, 16]

    def need_measurements():
        return not all(action in actions_taken for action in required_measurements)

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        if need_measurements():
            for action in required_measurements:
                if action not in actions_taken:
                    take_action(action)
                    break
            continue
            
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if events[3] == 0:
            take_action(3)
            continue

        if events[7] or (vitals["RespRate"] is not None and vitals["RespRate"] < 8):
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue

        if all(v is not None and v >= threshold for v, threshold in zip(
            [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
            [88, 8, 60])):
            take_action(48)
            break

        take_action(16)

if __name__ == "__main__":
    stabilize()
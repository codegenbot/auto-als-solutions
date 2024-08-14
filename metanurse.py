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

    def perform_ABC():
        for action in [3, 4, 5, 6, 7]:
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

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
        }

        if need_measurements():
            if 25 not in actions_taken:
                take_action(25)
                continue
            if 27 not in actions_taken:
                take_action(27)
                continue
            take_action(16)
            continue

        if vitals["MAP"] is None or vitals["Sats"] is None or vitals["RespRate"] is None:
            action = perform_ABC()
            take_action(action)
            continue

        if vitals["Sats"] < 65 or vitals["MAP"] < 20:
            take_action(22 if vitals["Sats"] < 65 else 17)
            continue

        if events[5] > 0 or events[4] > 0:
            take_action(31)
            continue

        if events[6] > 0:
            take_action(36)
            continue

        if vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] < 8:
            take_action(29)
            continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
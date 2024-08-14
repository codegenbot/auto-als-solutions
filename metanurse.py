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

    required_measurements = {25, 27, 16, 2}

    def need_measurements():
        return not required_measurements.issubset(actions_taken)

    def need_measurement_action():
        for action in required_measurements:
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

        if need_measurements():
            take_action(need_measurement_action())
            continue

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if events[3] == 0:
            take_action(3)
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(29)
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)
            continue
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if events[4] or events[5]:
            take_action(31)
            continue
        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(23)
            continue
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if any(events[i] > 0 for i in [28, 29, 30, 31, 32]):
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue

        take_action(48)


if __name__ == "__main__":
    stabilize()
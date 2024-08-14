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

    required_measurements = {25, 27, 16, 3}

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

        if any(events[i] > 0 for i in [4, 5, 6]):
            if events[5] > 0 or events[4] > 0:
                take_action(31)
            else:
                take_action(36 if events[6] > 0 else 32)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if any(events[i] > 0 for i in range(28, 33)):
                take_action(28)
                take_action(2)
                take_action(40)
                take_action(47)
                take_action(41)
            else:
                take_action(15)
            continue

        if all(vitals[key] is not None and min_value <= vitals[key] <= max_value for key, min_value, max_value in [
                ("Sats", 88, 100), ("RespRate", 8, 20), ("MAP", 60, 100)]):
            take_action(48)
            continue

        take_action(1)

if __name__ == "__main__":
    stabilize()
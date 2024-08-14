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

    required_measurements = {25, 27, 16, 3, 4, 5, 6}

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
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "CapillaryGlucose": vital_signs_values[2]
            if vital_signs_times[2] > 0
            else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
            "RespEffort": vital_signs_values[6] if vital_signs_times[6] > 0 else None,
        }

        airway_events = [events[i] for i in [3, 4, 5, 6]]
        breathing_events = [events[i] for i in [7, 8, 9, 10, 11, 12, 13, 14]]

        if any(breathing_events):
            take_action(4)
            continue

        if any(airway_events):
            take_action(3)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(23)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if any(events[i] > 0 for i in range(33)):
            take_action(8)
            continue

        take_action(48)


if __name__ == "__main__":
    stabilize()
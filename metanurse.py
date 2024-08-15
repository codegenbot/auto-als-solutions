import sys


def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    essential_measurements = [24, 25, 27, 26]

    def next_essential_measurement_action():
        for action in essential_measurements:
            if action not in actions_taken:
                return action

    def needs_essential_measurements():
        return not all(action in actions_taken for action in essential_measurements)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)
            continue

        if needs_essential_measurements():
            take_action(next_essential_measurement_action())
            continue

        if events[3] == 0:
            take_action(3)
            continue

        if vitals["Sats"] is None:
            take_action(25)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["MAP"] is None:
            take_action(27)
            continue

        if vitals["RR"] is None:
            take_action(25)
            continue

        if vitals["HR"] is None:
            take_action(2)
            continue

        if vitals["HR"] and vitals["HR"] > 150:
            take_action(40)
            take_action(41)
            take_action(47)
            take_action(43)
            continue

        if all(
            [
                vitals["HR"] and 60 <= vitals["HR"] <= 100,
                vitals["RR"] and 12 <= vitals["RR"] <= 20,
                vitals["MAP"] and vitals["MAP"] >= 60,
                vitals["Sats"] and vitals["Sats"] >= 88,
            ]
        ):
            take_action(48)
            break

        take_action(1)


if __name__ == "__main__":
    stabilize()
import sys


def stabilize():
    max_steps = 350
    steps_taken = 0

    def take_action(action):
        print(action)
        nonlocal steps_taken
        steps_taken += 1
        if steps_taken >= max_steps or action == 48:
            exit()

    taken_actions = set()

    for _ in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    [
                        "HeartRate",
                        "RespRate",
                        "CapillaryGlucose",
                        "Temperature",
                        "MAP",
                        "Sats",
                        "Resps",
                    ],
                    vital_signs_values,
                )
            )
        }

        if events[3] == 0:
            take_action(3)
            continue

        if events[7] > 0:
            take_action(29)
            continue

        if vitals["Sats"] is None:
            take_action(25)
            continue

        if vitals["RespRate"] is None:
            take_action(4)
            continue

        if vitals["MAP"] is None:
            take_action(27)
            continue

        if events[30] > 0 or events[31] > 0 or events[32] > 0:
            if 28 not in taken_actions:
                take_action(28)
                taken_actions.add(28)
                continue
            take_action(40)
            continue

        if vitals["MAP"] < 20 or vitals["Sats"] < 65:
            take_action(23)
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

        if vitals["MAP"] >= 60 and vitals["Sats"] >= 88 and vitals["RespRate"] >= 8:
            take_action(48)
            continue


if __name__ == "__main__":
    stabilize()
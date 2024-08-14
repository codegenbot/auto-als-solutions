import sys

def stabilize():
    max_steps = 350
    done = False

    def take_action(action):
        nonlocal done
        print(action)
        if action == 48:
            done = True

    required_measurements = [25, 27, 16, 2]

    def need_measurements(actions_taken):
        return not all(action in actions_taken for action in required_measurements)

    actions_taken = set()

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
            "CapillaryGlucose": vital_signs_values[2] if vital_signs_times[2] else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
            "Resps": vital_signs_values[6] if vital_signs_times[6] else None,
        }

        if need_measurements(actions_taken):
            for action in required_measurements:
                if action not in actions_taken:
                    actions_taken.add(action)
                    take_action(action)
                    break
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            continue

        if events[4] > 0 or events[5] > 0:
            take_action(31)
            continue
        if events[6] > 0:
            take_action(36)
            continue

        if events[7] > 0:
            take_action(29)
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if events[19] == 0:
            take_action(8)
            continue

        if vitals["MAP"] >= 60 and vitals["Sats"] >= 88 and vitals["RespRate"] >= 8:
            take_action(48)
            continue

        take_action(1)

if __name__ == "__main__":
    stabilize()
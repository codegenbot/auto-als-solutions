import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {25, 27, 16, 24}

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:  # Ensure proper input length
            take_action(48)
            continue

        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if required_measurements - actions_taken:
            take_action(next(iter(required_measurements - actions_taken)))
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(23)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if any(events[i] > 0 for i in range(30, 39)):  # Handle unstable tachyarrhythmias
                actions = [24, 40, 47, 45, 48]
                for action in actions:
                    if action not in actions_taken:
                        take_action(action)
                        break
            else:
                take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
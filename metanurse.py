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

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                     "MAP", "Sats", "Resps"], vital_signs_values
                )
            )
        }

        if 3 not in actions_taken:
            take_action(3)
            continue

        if events[3] == 0:
            take_action(3)
            continue

        if 5 not in actions_taken:
            take_action(5)
            continue

        if events[7] > 0:
            take_action(29)
            continue

        if 25 not in actions_taken:
            take_action(25)
            continue

        if 27 not in actions_taken:
            take_action(27)
            continue

        if 16 not in actions_taken:
            take_action(16)
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(22)
            continue

        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if vitals["HeartRate"] and vitals["HeartRate"] >= 150:
            if 28 not in actions_taken:
                take_action(28)
                continue
            if 47 not in actions_taken:
                take_action(47)
                continue
            continue

        if vitals["MAP"] and events[15] > 0:
            take_action(22)
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            take_action(48)
            return

        take_action(48)
        return

if __name__ == "__main__":
    stabilize()
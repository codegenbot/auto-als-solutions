import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    initial_measurements = [24, 25, 27, 26, 18, 19, 20, 21, 37]

    def take_action(action):
        print(action)
        actions_taken.add(action)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
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

        if any(action not in actions_taken for action in initial_measurements):
            for action in initial_measurements:
                if action not in actions_taken:
                    take_action(action)
                    break
            continue

        if all(vitals[key] is not None for key in vitals) and \
           vitals["Sats"] >= 88 and vitals["RR"] >= 8 and vitals["MAP"] >= 60:
            take_action(48)
            break

        if any(events[i] > 0 for i in [3, 4, 5, 6]):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            elif events[6] > 0:
                take_action(32)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        tachyarrhythmias = [27, 30, 28, 29, 34, 39]
        if any(events[i] > 0 for i in tachyarrhythmias):
            take_action(24)
            take_action(47)
            take_action(43)
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)
            continue

        take_action(7)

if __name__ == "__main__":
    stabilize()
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

    def need_measurements():
        required_measurements = {25, 27, 16, 3, 5, 38}
        return not required_measurements.issubset(actions_taken)

    def next_measurement_action():
        for action in {25, 27, 16, 3, 5, 38}:
            if action not in actions_taken:
                return action

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vitals_times, vitals_values = observations[:33], observations[33:40], observations[40:]

        if need_measurements():
            take_action(next_measurement_action())
            continue

        vitals = {
            "HeartRate": vitals_values[0] if vitals_times[0] > 0 else None,
            "RespRate": vitals_values[1] if vitals_times[1] > 0 else None,
            "MAP": vitals_values[4] if vitals_times[4] > 0 else None,
            "Sats": vitals_values[5] if vitals_times[5] > 0 else None,
        }

        if not events[3] and any(events[i] > 0 for i in range(4, 7)):
            take_action(31 if any(events[i] > 0 for i in (4, 5)) else 36)
            continue
        
        if any(events[i] > 0 for i in range(7, 15)) or (vitals["RespRate"] is not None and vitals["RespRate"] < 8):
            take_action(29 if vitals["RespRate"] < 8 else 30)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue
        if any(events[i] > 0 for i in range(28, 33)):
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(43)
            continue

        if vitals["Sats"] is not None:
            if vitals["Sats"] < 65:
                take_action(22)
                continue
            if vitals["Sats"] < 88:
                take_action(30)
                continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
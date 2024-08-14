import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action, break_action=True):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True
        return break_action

    def need_measurements():
        return (
            25 not in actions_taken
            or 27 not in actions_taken
            or 16 not in actions_taken
            or 3 not in actions_taken
        )

    def need_measurement_action():
        if 25 not in actions_taken:
            return 25
        if 27 not in actions_taken:
            return 27
        if 16 not in actions_taken:
            return 16
        if 3 not in actions_taken:
            return 3
        return None

    def update_vitals(vital_signs_times, vital_signs_values):
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
        }
        return vitals

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = update_vitals(vital_signs_times, vital_signs_values)

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            if take_action(17):
                continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            if take_action(22):
                continue

        if need_measurements():
            measurement_action = need_measurement_action()
            if measurement_action is not None:
                if take_action(measurement_action):
                    continue

        vitals = update_vitals(vital_signs_times, vital_signs_values)

        if events[4] > 0 or events[5] > 0:
            if take_action(31):
                continue

        if events[6] > 0:
            if take_action(36):
                continue

        if events[7] > 0:
            if take_action(29):
                continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if take_action(15):
                continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            if take_action(29):
                continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if take_action(30):
                continue
        
        if any(events[i] > 0 for i in range(28, 38)):
            if 28 not in actions_taken:
                if take_action(28):
                    continue
            if take_action(40):
                continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60 and all(events[i] == 0 for i in range(28, 38)):
            if take_action(15):
                continue

        if all([
            vitals["Sats"] is not None and vitals["Sats"] >= 88,
            vitals["RespRate"] is not None and vitals["RespRate"] >= 8,
            vitals["MAP"] is not None and vitals["MAP"] >= 60
        ]):
            if take_action(48, False):
                break

if __name__ == "__main__":
    stabilize()
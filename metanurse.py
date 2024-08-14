import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "CapillaryGlucose": vital_signs_values[2] if vital_signs_times[2] > 0 else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
            "Resps": vital_signs_values[6] if vital_signs_times[6] > 0 else None
        }

        def take_action(action):
            actions_taken.add(action)
            print(action)

        def examine_if_needed():
            if 25 not in actions_taken:
                take_action(25)
                return True
            if 27 not in actions_taken:
                take_action(27)
                return True
            if 16 not in actions_taken:
                take_action(16)
                return True
            if 3 not in actions_taken:
                take_action(3)
                return True
            if 4 not in actions_taken:
                take_action(4)
                return True
            if 5 not in actions_taken:
                take_action(5)
                return True
            return False

        if examine_if_needed():
            continue

        unstable_tachyarrhythmia = any(events[i] > 0 for i in [29, 30, 31, 33, 34, 35, 36])

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue

        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
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
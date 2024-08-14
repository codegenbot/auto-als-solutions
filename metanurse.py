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
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                [
                    "HeartRate",
                    "RespRate",
                    "CapillaryGlucose",
                    "Temperature",
                    "MAP",
                    "Sats",
                    "Resps"
                ]
            )
        }

        def take_action(action):
            actions_taken.add(action)
            print(action)

        # Handle immediate life threats first
        if events[29] > 0 or events[30] > 0 or events[31] > 0:  # unstable tachyarrhythmia
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue

        # ABCDE Examination flow - loop through
        for exam in [25, 27, 16, 3, 4, 5, 8, 2]:
            if exam not in actions_taken:
                take_action(exam)
                break
        
        # Handle stabilizing actions
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        # Check for stable condition
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

if __name__ == "__main__":
    stabilize()
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

        # AB - Check vitals first
        if 25 not in actions_taken:
            take_action(25)
            continue
        if 27 not in actions_taken:
            take_action(27)
            continue
        if 16 not in actions_taken:
            take_action(16)
            continue
        
        # Conduct necessary examinations
        necessary_examinations = [3, 4, 5, 8, 2]
        for exam in necessary_examinations:
            if exam not in actions_taken:
                take_action(exam)
                break

        unstable_tachyarrhythmia = events[29] > 0 or events[30] > 0 or events[31] > 0

        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(22)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60 and not unstable_tachyarrhythmia:
            take_action(15)
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue
        
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
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
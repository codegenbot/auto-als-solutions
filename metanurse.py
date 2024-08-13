import sys

def stabilize():
    max_steps = 350
    steps_examine = [3, 4, 5, 25, 27, 16]

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
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
                    "Resps",
                ],
            )
        }

        critical_actions = [(vitals["Sats"], 65, 17), 
                            (vitals["MAP"], 20, 17), 
                            (vitals["HeartRate"], 50, 24)]

        for critical_vital, threshold, action in critical_actions:
            if critical_vital is not None and (critical_vital < threshold or critical_vital > 150):
                print(action)
                break

        if step < len(steps_examine):
            print(steps_examine[step])
        elif vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)
        elif vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
        elif vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
        elif vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            print(24)
        elif all(vital is not None and vital >= threshold
                for vital, threshold in zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            print(48)
            return
        else:
            print(1)

if __name__ == "__main__":
    stabilize()
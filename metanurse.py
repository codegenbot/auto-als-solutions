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
                    "Resps",
                ],
            )
        }

        initial_exams = [25, 27, 16, 3, 4, 5, 6, 7, 2]
        for action in initial_exams:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                break
        else:
            if vitals["Sats"] and vitals["Sats"] < 65:
                print(22)
            elif vitals["MAP"] and vitals["MAP"] < 20:
                print(15)
            elif vitals["MAP"] and vitals["MAP"] < 60:
                print(15)
            elif vitals["Sats"] and vitals["Sats"] < 88:
                print(30)
            elif vitals["RespRate"] and vitals["RespRate"] < 8:
                print(29)
            elif events[29] > 0 or events[30] > 0:
                print(10)
            elif all(vital is not None and vital >= threshold for vital, threshold in zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
                print(48)
                return
            else:
                print(48)
                return

if __name__ == "__main__":
    stabilize()
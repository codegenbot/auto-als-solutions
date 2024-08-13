import sys

def stabilize():
    max_steps = 350
    actions_taken = []

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
                    "HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                    "MAP", "Sats", "Resps"
                ]
            )
        }

        # Initial assessments
        if step == 0:
            actions_taken.append(3); print(3); continue
        elif step == 1:
            actions_taken.append(25); print(25); continue
        elif step == 2:
            actions_taken.append(27); print(27); continue
        elif step == 3:
            actions_taken.append(16); print(16); continue
        elif step == 4:
            actions_taken.append(26); print(26); continue
        elif step == 5:
            actions_taken.append(4); print(4); continue

        # Stabilization actions
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17); continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17); continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15); continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30); continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29); continue
        if vitals["HeartRate"] is not None:
            if vitals["HeartRate"] > 150:
                print(9); continue
            elif vitals["HeartRate"] < 50:
                print(13); continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48); return

        print(48); return

if __name__ == "__main__":
    stabilize()
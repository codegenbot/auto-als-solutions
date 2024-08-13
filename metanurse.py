import sys

def main():
    max_steps = 350
    initial_examine = False
    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "CapillaryGlucose": vital_signs_values[2] if vital_signs_times[2] > 0 else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
            "Resps": vital_signs_values[6] if vital_signs_times[6] > 0 else None
        }

        if not initial_examine:
            action = [3, 4, 5][step % 3]
            print(action)
            if step % 3 == 2:
                initial_examine = True
            continue

        if "UseSatsProbe" not in actions_taken:
            print(25)
            actions_taken.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in actions_taken:
            print(27)
            actions_taken.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in actions_taken:
            print(16)
            actions_taken.add("ViewMonitor")
            continue

        if vitals["Sats"] is not None and (vitals["Sats"] < 65 or (vitals["MAP"] is not None and vitals["MAP"] < 20)):
            print(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
                if "TurnOnDefibrillator" not in actions_taken:
                    print(39)
                    actions_taken.add("TurnOnDefibrillator")
                    continue
                print(40)
                continue
            print(15)
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return

    print(48)

if __name__ == "__main__":
    main()
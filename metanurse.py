import sys

def main():
    max_steps = 350
    step_sequence = [
        3, 4, 5, 6, 7,  # Initial ABCDE exam
        25, 27, 38, 16   # Use Sats probe, BP cuff, measure BP, view monitor
    ]
    step_idx = 0
    used_methods = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )

        vitals = {
            name: value if time > 0 else None for value, time, name in zip(
                vital_signs_values, vital_signs_times, [
                    "HeartRate", "RespRate", "CapillaryGlucose", 
                    "Temperature", "MAP", "Sats", "Resps"
                ]
            )
        }

        if step_idx < len(step_sequence):
            print(step_sequence[step_idx])
            step_idx += 1
            continue

        needs_chest_compression = (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20)
        if needs_chest_compression:
            print(17)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)
            continue

        if ("ViewMonitor" in used_methods) and (vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50) or events[27]):
            if "TurnOnDefibrillator" not in used_methods:
                print(39)
                used_methods.add("TurnOnDefibrillator")
                continue
            elif "DefibrillatorCharge" not in used_methods:
                print(40)
                used_methods.add("DefibrillatorCharge")
                continue
            elif "DefibrillatorSync" not in used_methods:
                print(47)
                used_methods.add("DefibrillatorSync")
                continue
            else:
                print(43)
                continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return

        print(48)
        return

if __name__ == "__main__":
    main()
import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )
        vitals = {
            name: (value if time > 0 else None)
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

        # Initial examinations
        if step == 0 or not initial_examine:
            print([3, 4, 5, 8][step % 4])
            initial_examine = True
            continue

        # Airway Management
        if not events[3]:  # AirwayClear
            print(35)
            continue

        # Measure vitals if not done yet
        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue

        # Critical interventions
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)
            continue

        # Treat breathing issues
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue

        # Administer fluids for low blood pressure
        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)
            continue

        # Final checks before finishing
        if all(vital is not None and vital >= threshold for vital, threshold in zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            print(48)
            return

        # Default action
        print(48)
        return

if __name__ == "__main__":
    main()
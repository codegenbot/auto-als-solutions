import sys


def main():
    max_steps = 350
    used_methods = set()

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

        if not used_methods:
            print(3)  # ExamineAirway
            used_methods.add("ExamineAirway")
            continue

        if "ExamineAirway" in used_methods and "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue

        if "UseSatsProbe" in used_methods and vitals["Sats"] is None:
            print(4)  # ExamineBreathing to observe respiration
            used_methods.add("ExamineBreathing")
            continue

        if "ExamineBreathing" in used_methods and vitals["Sats"] is not None:
            if vitals["Sats"] < 65 or (
                vitals["MAP"] is not None and vitals["MAP"] < 20
            ):
                print(17)  # StartChestCompression
                continue
            if vitals["Sats"] < 88:
                print(30)  # UseNonRebreatherMask
                continue

        if (
            "ExamineBreathing" in used_methods
            and "UseBloodPressureCuff" not in used_methods
        ):
            print(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
            continue

        if "UseBloodPressureCuff" in used_methods and "ViewMonitor" not in used_methods:
            print(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
            continue

        if "ViewMonitor" in used_methods and vitals["MAP"] is not None:
            if vitals["MAP"] < 60:  # Treat hypotension
                if vitals["HeartRate"] is not None and (
                    vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50
                ):
                    if "TurnOnDefibrillator" not in used_methods:
                        print(39)  # TurnOnDefibrillator
                        used_methods.add("TurnOnDefibrillator")
                        continue
                    if "DefibrillatorCharge" not in used_methods:
                        print(40)  # DefibrillatorCharge
                        used_methods.add("DefibrillatorCharge")
                        continue
                    print(43)  # DefibrillatorPace
                    continue
                print(15)  # GiveFluids
                continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return
        else:
            print(48)  # If stabilization criteria aren't met, finish anyway
            return


if __name__ == "__main__":
    main()
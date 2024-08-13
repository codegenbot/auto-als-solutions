import sys


def main():
    max_steps = 350
    actions_taken = set()

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

        if step == 0:
            print(3)  # ExamineAirway
            actions_taken.add(3)
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

        if vitals["Sats"] is not None and (
            vitals["Sats"] < 65 or (vitals["MAP"] is not None and vitals["MAP"] < 20)
        ):
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
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

        print(48)  # Finish
        return


if __name__ == "__main__":
    main()
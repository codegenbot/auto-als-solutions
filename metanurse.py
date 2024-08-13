import sys


def main():
    max_steps = 350
    steps_taken = 0
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

        if steps_taken == 0:
            print(3)  # ExamineAirway
            steps_taken += 1
            continue

        if not events[3]:  # AirwayClear
            print(35)  # PerformAirwayManoeuvres
            continue

        if "UseSatsProbe" not in actions_taken:
            print(25)  # UseSatsProbe
            actions_taken.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in actions_taken:
            print(27)  # UseBloodPressureCuff
            actions_taken.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in actions_taken:
            print(16)  # ViewMonitor
            actions_taken.add("ViewMonitor")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        print(48)  # Finish
        return

    print(48)


if __name__ == "__main__":
    main()
import sys


def stabilize():
    max_steps = 350
    used_probes = set()

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

        if "ExamineAirway" not in used_probes:
            print(3)  # ExamineAirway
            used_probes.add("ExamineAirway")
            continue

        if "UseSatsProbe" not in used_probes:
            print(25)  # UseSatsProbe
            used_probes.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_probes:
            print(27)  # UseBloodPressureCuff
            used_probes.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in used_probes:
            print(16)  # ViewMonitor
            used_probes.add("ViewMonitor")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
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

        if vitals["HeartRate"] is not None:
            if vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50:
                print(39)  # TurnOnDefibrillator
                continue
            if 60 <= vitals["HeartRate"] <= 100:
                print(43)  # DefibrillatorPace
                continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(1)  # DoNothing


if __name__ == "__main__":
    stabilize()
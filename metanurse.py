import sys


def main():
    max_steps = 350
    examined_once = False

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

        if step == 0 or not examined_once:
            for action in [3, 4, 5]:  # Examine Airway, Breathing, Circulation
                print(action)
                examined_once = True
                break
            continue

        actions_checked = ["UseSatsProbe", "UseBloodPressureCuff", "ViewMonitor"]
        for action, flag in zip([25, 27, 16], actions_checked):
            if flag not in locals():
                print(action)
                locals()[flag] = True
                continue

        # Cardiac arrest situation
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            print(17)  # StartChestCompression
            continue

        # Treat breathing issues
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        # Treat circulation issues
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if vitals["HeartRate"] is not None and (
                vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50
            ):
                if "TurnOnDefibrillator" not in locals():
                    print(39)
                    locals()["TurnOnDefibrillator"] = True
                    continue
                if "DefibrillatorCharge" not in locals():
                    print(40)
                    locals()["DefibrillatorCharge"] = True
                    continue
                print(43)  # DefibrillatorPace
                continue
            print(15)  # GiveFluids
            continue

        # Check if patient is stabilized
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)
            return

    # Finish if maximum steps reached
    print(48)


if __name__ == "__main__":
    main()
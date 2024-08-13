import sys


def stabilize():
    max_steps = 350
    first_examine = True
    use_sats_probe = use_blood_pressure_cuff = view_monitor = False
    actions = iter([3, 4, 8, 7])  # Initial series of Examine actions
    assessments_done = set()  # Track completed assessments

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

        if first_examine:
            try:
                next_assessment = next(actions)
                assessments_done.add(next_assessment)
                print(next_assessment)
                continue
            except StopIteration:
                first_examine = False

        # Handle critical values
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        # Use equipment
        if not use_sats_probe:
            print(25)  # UseSatsProbe
            use_sats_probe = True
            continue

        if not use_blood_pressure_cuff:
            print(27)  # UseBloodPressureCuff
            use_blood_pressure_cuff = True
            continue

        if not view_monitor:
            print(16)  # ViewMonitor
            view_monitor = True
            continue

        # Provide treatments
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["HeartRate"] is not None and (
            vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50
        ):
            print(24)  # UseMonitorPads
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
    stabilize()
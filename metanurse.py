import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                 "MAP", "Sats", "Resps"]
            )
        }

        # Initial examinations
        if step == 0: actions_taken.add(25); print(25); continue  # UseSatsProbe
        if step == 1: actions_taken.add(27); print(27); continue  # UseBloodPressureCuff
        if step == 2: actions_taken.add(16); print(16); continue  # ViewMonitor
        if all(a in actions_taken for a in [25, 27, 16]):
            if "AirwayClear" not in actions_taken:
                print(3)  # ExamineAirway
                actions_taken.add("AirwayClear")
                continue

        # Interventions
        if vitals["Sats"] and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        # End criteria
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
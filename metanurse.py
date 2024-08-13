import sys

def stabilize():
    max_steps = 350
    actions = [3, 4, 5, 25, 27, 16]  # ExamineAirway, ExamineBreathing, ExamineCirculation, UseSatsProbe, UseBloodPressureCuff, ViewMonitor
    current_action = 0

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

        # First handle initial checks
        if current_action < len(actions):
            print(actions[current_action])
            current_action += 1
            continue

        # Intervene if critical
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            print(17)  # StartChestCompression
            continue

        # Handle interventions based on observations
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        # Check if stabilized
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(1)  # DoNothing and continue checking

if __name__ == "__main__":
    stabilize()
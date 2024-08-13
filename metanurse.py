import sys

def stabilize():
    max_steps = 350
    steps_taken = 0

    actions_taken = set()
    check_vitals_actions = [25, 27, 16]  # SatsProbe, BloodPressureCuff, ViewMonitor
    examine_actions = [5, 3, 4, 8, 2]  # Circulation, Airway, Breathing, Response, CheckRhythm

    while steps_taken < max_steps:
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

        for action in check_vitals_actions:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                steps_taken += 1
                break
        else:
            for action in examine_actions:
                if action not in actions_taken:
                    actions_taken.add(action)
                    print(action)
                    steps_taken += 1
                    break
            else:
                if vitals["MAP"] and vitals["MAP"] < 20:
                    print(17)  # StartChestCompression
                elif vitals["Sats"] and vitals["Sats"] < 65:
                    print(22)  # BagDuringCPR
                elif vitals["MAP"] and vitals["MAP"] < 60:
                    print(15)  # GiveFluids
                elif vitals["Sats"] and vitals["Sats"] < 88:
                    print(30)  # UseNonRebreatherMask
                elif vitals["RespRate"] and vitals["RespRate"] < 8:
                    print(29)  # UseBagValveMask
                elif all(vital is not None and vital >= threshold
                         for vital, threshold in zip(
                             [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                             [88, 8, 60])):
                    print(48)  # Finish
                    return
                steps_taken += 1

if __name__ == "__main__":
    stabilize()
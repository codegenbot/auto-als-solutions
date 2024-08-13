import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    action_order = [
        (25, False), # UseSatsProbe
        (27, False), # UseBloodPressureCuff
        (16, False), # ViewMonitor
        (5, False),  # ExamineCirculation
        (3, False),  # ExamineAirway
        (4, False),  # ExamineBreathing
        (8, False),  # ExamineResponse
        (2, False)   # CheckRhythm
    ]

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

        for i in range(len(action_order)):
            action, taken = action_order[i]
            if not taken:
                actions_taken.add(action)
                print(action)
                action_order[i] = (action, True)
                break
        else:
            if vitals["MAP"] and vitals["MAP"] < 20:
                print(17)  # StartChestCompression
                continue
            if vitals["Sats"] and vitals["Sats"] < 65:
                print(22)  # BagDuringCPR
                continue
            if any(events[i] > 0 for i in range(29, 37)):
                print(9)  # GiveAdenosine
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

            if all(
                vital is not None and vital >= threshold
                for vital, threshold in zip(
                    [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                    [88, 8, 60]
                )
            ):
                print(48)
                return

            print(48)
            return

if __name__ == "__main__":
    stabilize()
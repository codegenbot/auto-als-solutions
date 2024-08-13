import sys

def stabilize():
    max_steps = 350

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        # Map vitals
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

        # Ensure Airway is clear
        if events[3] == 0:
            print(3)  # ExamineAirway
            continue

        # Sudden critical drop checks
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # Bag During CPR
            continue

        # Take necessary initial actions
        for action in (25, 27, 16, 3, 4, 5, 8, 2):
            print(action)
            continue
        
        # Check vitals and stabilize
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        unstable_tachyarrhythmia = events[29] > 0 or events[30] > 0 or events[32] > 0
        if unstable_tachyarrhythmia:
            if events[28] == 0:
                print(28)  # AttachDefibPads
            else:
                print(41)  # DefibrillatorCurrentUp
            continue

        # Check if patient is stabilized
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
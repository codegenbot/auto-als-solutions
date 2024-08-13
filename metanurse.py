import sys

def stabilize():
    max_steps = 350
    
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

        # Critical conditions
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression for critically low Sats
            return
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression for critically low MAP
            return

        # Interventions for stabilizing
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        # Initial examinations to retrieve required vitals
        initial_exams = [25, 27, 16, 3, 4, 5, 6]  # Removed CheckRhythm to focus on essentials
        for action in initial_exams:
            print(action)
            break

        # End criteria - if vital signs are stable, indicate completion.
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

    print(48)  # Finish by default to avoid infinite loop

if __name__ == "__main__":
    stabilize()
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
        initial_exams = [25, 27, 16, 3, 4, 5, 6]
        for action in initial_exams:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                sys.stdout.flush()
                break

        # Interventions
        if vitals["Sats"] and vitals["Sats"] < 65 or vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            sys.stdout.flush()
            continue
        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            sys.stdout.flush()
            continue
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            sys.stdout.flush()
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            sys.stdout.flush()
            continue
        
        # Add cardioversion if unstable tachyarrhythmia detected
        unstable_tachyarrhythmia = [
            'HeartRhythmSVT', 'HeartRhythmVT', 'HeartRhythmAF', 'HeartRhythmAtrialFlutter'
        ]
        if any(events[i] > 0 for i in range(38, 42)):
            print(10)  # e.g., cardioversion action like `GiveAdrenaline`
            sys.stdout.flush()
            continue

        # End criteria - if vital signs are stable, indicate completion.
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            sys.stdout.flush()
            return

        print(0)  # DoNothing by default to progress loop without Finish.
        sys.stdout.flush()

if __name__ == "__main__":
    stabilize()
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

        # Prioritize immediate critical actions
        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # BagDuringCPR
            continue
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(15)  # GiveFluids
            continue
        if vitals["MAP"] and vitals["MAP"] < 60:
            if events[29] > 0 or events[30] > 0:  # HeartRhythmSVT or HeartRhythmAF
                print(10)  # GiveAmiodarone
                continue
            else:
                print(15)  # GiveFluids
                continue
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue
        if events[29] > 0 or events[30] > 0:  # HeartRhythmSVT or HeartRhythmAF
            print(10)  # GiveAmiodarone
            continue

        # Perform standard examinations if critical actions are not required
        next_steps = [
            (25, "UseSatsProbe"),
            (27, "UseBloodPressureCuff"),
            (16, "ViewMonitor"),
            (3, "ExamineAirway"),
            (4, "ExamineBreathing"),
            (5, "ExamineCirculation"),
            (6, "ExamineDisability"),
            (7, "ExamineExposure"),
            (2, "CheckRhythm")
        ]

        for action_code, _ in next_steps:
            if action_code not in actions_taken:
                actions_taken.add(action_code)
                print(action_code)
                break  # Perform next action
        else:
            if all(
                vital is not None and vital >= threshold
                for vital, threshold in zip(
                    [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
                )
            ):
                print(48)  # Finish
                break

if __name__ == "__main__":
    stabilize()
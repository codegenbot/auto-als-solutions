import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
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

        # Initial examinations
        initial_exams = [25, 27, 16, 3, 4, 5, 6, 7, 2]  # Order of examinations
        for action in initial_exams:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                break
        else:
            # Interventions based on vitals
            if vitals["Sats"] and vitals["Sats"] < 65:
                print(22)  # Bag During CPR
            elif vitals["MAP"] and vitals["MAP"] < 20:
                print(15)  # GiveFluids
            elif vitals["MAP"] and vitals["MAP"] < 60:
                print(15)  # GiveFluids
            elif vitals["Sats"] and vitals["Sats"] < 88:
                print(30)  # UseNonRebreatherMask
            elif vitals["RespRate"] and vitals["RespRate"] < 8:
                print(29)  # UseBagValveMask
            elif events[29] > 0 or events[30] > 0:  # HeartRhythmSVT or HeartRhythmAF
                print(10)  # GiveAmiodarone (for SVT or AF)
            elif all(vital is not None and vital >= threshold for vital, threshold in zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
                print(48)  # Finish
                return
            else:
                print(48)  # Finish
                return

if __name__ == "__main__":
    stabilize()
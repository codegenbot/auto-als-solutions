import sys


def stabilize():
    max_steps = 350
    actions_taken = set()

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

        if 25 not in actions_taken:
            actions_taken.add(25)
            print(25)  # UseSatsProbe
            continue
        if 27 not in actions_taken:
            actions_taken.add(27)
            print(27)  # UseBloodPressureCuff
            continue
        if 16 not in actions_taken:
            actions_taken.add(16)
            print(16)  # ViewMonitor
            continue
        if 3 not in actions_taken:
            actions_taken.add(3)
            print(3)  # ExamineAirway
            continue
        if 4 not in actions_taken:
            actions_taken.add(4)
            print(4)  # ExamineBreathing
            continue
        if 5 not in actions_taken:
            actions_taken.add(5)
            print(5)  # ExamineCirculation
            continue
        if 8 not in actions_taken:
            actions_taken.add(8)
            print(8)  # ExamineResponse
            continue
        if 2 not in actions_taken:
            actions_taken.add(2)
            print(2)  # CheckRhythm
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # Bag During CPR
            continue
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(15)  # GiveFluids
            continue
        if vitals["MAP"] and vitals["MAP"] < 60:
            if events[29] > 0 or events[30] > 0:  # HeartRhythmSVT or HeartRhythmAF
                print(10)  # GiveAmiodarone
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
            print(10)  # GiveAmiodarone (for SVT or AF)
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
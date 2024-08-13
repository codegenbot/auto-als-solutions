import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                 "MAP", "Sats", "Resps"]
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
        if 6 not in actions_taken:
            actions_taken.add(6)
            print(6)  # ExamineDisability
            continue
        if 7 not in actions_taken:
            actions_taken.add(7)
            print(7)  # ExamineExposure
            continue
        if 2 not in actions_taken:
            actions_taken.add(2)
            print(2)  # CheckRhythm
            continue
            
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

if __name__ == "__main__":
    stabilize()
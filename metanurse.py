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
        
        if step == 0:
            print(3)  # ExamineAirway
        elif step == 1:
            print(4)  # ExamineBreathing
        elif step == 2:
            print(5)  # ExamineCirculation
        elif step == 3:
            print(6)  # ExamineDisability
        elif step == 4:
            print(7)  # ExamineExposure
        elif step == 5:
            print(2)  # CheckRhythm
        else:
            if vitals["Sats"] and vitals["Sats"] < 65:
                print(22)  # BagDuringCPR
            elif vitals["MAP"] and vitals["MAP"] < 20:
                print(15)  # GiveFluids
            elif vitals["MAP"] and vitals["MAP"] < 60:
                print(15)  # GiveFluids
            elif vitals["Sats"] and vitals["Sats"] < 88:
                print(30)  # UseNonRebreatherMask
            elif vitals["RespRate"] and vitals["RespRate"] < 8:
                print(29)  # UseBagValveMask
            elif vitals["HeartRate"] and (events[29] > 0 or events[30] > 0):  # HeartRhythmSVT or HeartRhythmAF
                print(10)  # GiveAmiodarone
            elif all(
                vital is not None and vital >= threshold
                for vital, threshold in zip(
                    [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
                )
            ):
                print(48)  # Finish
                break
            else:
                print(0)  # DoNothing

if __name__ == "__main__":
    stabilize()
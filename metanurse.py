import sys

def main():
    max_steps = 350
    used_methods = set()
    step = 0

    while step < max_steps:
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

        if step == 0:
            print(3)  # ExamineAirway
        elif not events[3]:  # AirwayClear event
            print(35)  # PerformAirwayManoeuvres
        elif "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
        elif "UseBloodPressureCuff" not in used_methods:
            print(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
        elif vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
        elif "ViewMonitor" not in used_methods:
            print(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
        elif (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # StartChestCompression
        elif vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
        elif vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
        elif vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            if "TurnOnDefibrillator" not in used_methods:
                print(39)  # TurnOnDefibrillator
                used_methods.add("TurnOnDefibrillator")
            elif "DefibrillatorCurrentUp" not in used_methods:
                print(41)  # DefibrillatorCurrentUp
                used_methods.add("DefibrillatorCurrentUp")
            else:
                print(43)  # DefibrillatorPace
        elif all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return
        else:
            print(48)  # Finish, just in case
            return
        
        step += 1  # Increment step counter for each loop iteration

if __name__ == "__main__":
    main()
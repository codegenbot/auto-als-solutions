import sys

def main():
    max_steps = 350
    step = 0
    used_methods = set()
    initial_examine_done = False

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
            initial_examine_done = True
        elif not events[3]:  # AirwayClear event hasn't occurred
            print(35)  # PerformAirwayManoeuvres
        elif "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
        elif "UseBloodPressureCuff" not in used_methods:
            print(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
        elif "ViewMonitor" not in used_methods:
            print(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
        elif vitals["Sats"] is not None and vitals["Sats"] < 65 or vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
        elif vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
        elif any(events[28:35]) and vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            if "TurnOnDefibrillator" not in used_methods:
                print(39)  # TurnOnDefibrillator
                used_methods.add("TurnOnDefibrillator")
            elif "DefibrillatorCharge" not in used_methods:
                print(40)  # DefibrillatorCharge
                used_methods.add("DefibrillatorCharge")
            elif "DefibrillatorSync" not in used_methods:
                print(47)  # DefibrillatorSync
                used_methods.add("DefibrillatorSync")
            else:
                print(43)  # DefibrillatorPace
        elif vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
        elif vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
        elif all(vital is not None and vital >= threshold for vital, threshold in zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            print(48)  # Finish
            return
        else:
            print(48)  # Finish, just in case
            return
        
        step += 1

if __name__ == "__main__":
    main()
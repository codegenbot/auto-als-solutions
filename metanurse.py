import sys
import math

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False

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

        if step == 0 or not initial_examine:
            print(3)  # ExamineAirway
            initial_examine = True
            continue

        if not events[3]:  # AirwayClear
            print(35)  # PerformAirwayManoeuvres
            continue

        if "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            print(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50) or (
            events[28] or events[29] or events[30]
        ):  # Unstable tachyarrhythmia
            if "TurnOnDefibrillator" not in used_methods:
                print(39)  # TurnOnDefibrillator
                used_methods.add("TurnOnDefibrillator")
                continue
            elif "DefibrillatorCharge" not in used_methods:
                print(40)  # DefibrillatorCharge
                used_methods.add("DefibrillatorCharge")
                continue
            elif "DefibrillatorSync" not in used_methods:
                print(47)  # DefibrillatorSync
                used_methods.add("DefibrillatorSync")
                continue
            else:
                print(43)  # DefibrillatorPace
                continue

        if step >= max_steps - 1:
            print(48)  # Finish if near max steps
            return

    print(48)  # Finish if no issues
    return

if __name__ == "__main__":
    main()
import sys

def main():
    max_steps = 350
    used_methods = set()

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
                vital_signs_times, [
                    "HeartRate",
                    "RespRate",
                    "CapillaryGlucose",
                    "Temperature",
                    "MAP",
                    "Sats",
                    "Resps"
                ]
            )
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # StartChestCompression
            continue

        if step == 0 or "InitialExamine" not in used_methods:
            print(3)  # ExamineAirway
            used_methods.add("InitialExamine")
            continue

        if not events[3]:  # Not AirwayClear
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
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 60):
            print(40)  # DefibrillatorCharge
            continue

        if all([
            events[3],  # Airway Clear
            vitals["Sats"] is not None and vitals["Sats"] >= 88,  # Sats >= 88%
            vitals["RespRate"] is not None and vitals["RespRate"] >= 8,  # Resp Rate >= 8
            vitals["MAP"] is not None and vitals["MAP"] >= 60  # MAP >= 60
        ]):
            print(48)  # Finish
            return

        print(1)  # DoNothing or CheckSignsOfLife; this is a fallback action

if __name__ == "__main__":
    main()
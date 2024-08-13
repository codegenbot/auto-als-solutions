import sys

def main():
    max_steps = 350
    used_methods = set()
    observations_needed = {"AirwayClear", "RespRate", "MeasuredSats", "MeasuredMAP"}

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

        if step == 0:
            print(3)  # Initial Airway Examination
            continue

        # Ensure airway is clear
        if not events[3]:  # Ensure AirwayClear
            print(35)  # PerformAirwayManoeuvres
            continue
        
        # Breathing examination
        if not events[10]:
            print(4)  # ExamineBreathing
            continue

        # Use Sats probe
        if "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue
        
        # View Monitor for the Sats Probe reading
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

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)  # GiveAtropine
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(2)  # CheckRhythm
                continue
            elif vitals["HeartRate"] > 150:
                print(11)  # GiveAmiodarone
                continue
            
        if all(vitals[k] and vitals[k] >= v for k, v in {
            "Sats": 88, "RespRate": 8, "MAP": 60
        }.items()):
            print(48)  # Finish
            return

        print(0)  # DoNothing

    print(48)  # Just in case, finish anyway

if __name__ == "__main__":
    main()
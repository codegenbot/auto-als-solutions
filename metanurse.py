import sys

def main():
    max_steps = 350
    used_methods = set()

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

        if not events[3]:  # Ensure airway is clear
            print(35)
            continue

        if "OpenBreathingDrawer" not in used_methods:
            print(19)
            used_methods.add("OpenBreathingDrawer")
            continue

        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)
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

        print(48)
        return

    print(48)

if __name__ == "__main__":
    main()
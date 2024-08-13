import sys

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
            print(3)
            initial_examine = True
            continue

        # Check Airway
        if not events[3]:  # !AirwayClear
            print(35)  # PerformAirwayManoeuvres
            continue

        # Ensure all measurements are taken
        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue

        # Critical conditions
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # StartChestCompression
            continue

        # Non-critical stabilisation criteria
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if (vitals["HeartRate"] and vitals["HeartRate"] > 150) or events[27]:  # !StablePulse
            print(40)  # DefibrillatorCharge
            continue

        # If stabilised
        if (vitals["Sats"] and vitals["Sats"] >= 88) and (vitals["RespRate"] and vitals["RespRate"] >= 8) and (vitals["MAP"] and vitals["MAP"] >= 60):
            print(48)  # Finish
            return

    print(48)  # Finish after max_steps

if __name__ == "__main__":
    main()
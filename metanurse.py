import sys

def main():
    max_steps = 350
    observed = set()
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
                vital_signs_times,
                [
                    "HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                    "MAP", "Sats", "Resps"
                ]
            )
        }

        if step == 0:
            print(3)  # ExamineAirway
            continue
        
        if not events[3]:  # If airway not clear
            print(35)  # PerformAirwayManoeuvres
            continue

        if step == 1 or "SatsProbe" not in observed:
            print(25)  # UseSatsProbe
            observed.add("SatsProbe")
            continue
        
        if step == 2 or "BloodPressureCuff" not in observed:
            print(27)  # UseBloodPressureCuff
            observed.add("BloodPressureCuff")
            continue

        if step == 3 or "ViewMonitor" not in observed:
            print(16)  # ViewMonitor
            observed.add("ViewMonitor")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # StartChestCompression
            continue

        if vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50) and "DefibTurnedOn" not in observed:
            print(39)  # TurnOnDefibrillator
            observed.add("DefibTurnedOn")
            continue

        if "DefibTurnedOn" in observed and "DefibCharged" not in observed:
            print(40)  # DefibrillatorCharge
            observed.add("DefibCharged")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            print(48)  # Finish
            return

    print(48)  # Finish as fallback

if __name__ == "__main__":
    main()
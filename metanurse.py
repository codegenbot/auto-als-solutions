import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False
    steps_taken = []

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
                    "HeartRate", "RespRate", "CapillaryGlucose",
                    "Temperature", "MAP", "Sats", "Resps",
                ],
            )
        }

        if step == 0 or not initial_examine:
            steps_taken.append(3)  # ExamineAirway
            initial_examine = True
            continue

        if not events[3]:  # AirwayClear
            steps_taken.append(35)  # PerformAirwayManoeuvres
            continue

        if "UseSatsProbe" not in used_methods:
            steps_taken.append(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            steps_taken.append(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in used_methods:
            steps_taken.append(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            steps_taken.append(17)  # StartChestCompression
            continue

        if vitals.get("Sats") is not None and vitals["Sats"] < 88:
            steps_taken.append(30)  # UseNonRebreatherMask
            continue

        if vitals.get("RespRate") is not None and vitals["RespRate"] < 8:
            steps_taken.append(29)  # UseBagValveMask
            continue

        if vitals.get("MAP") is not None and vitals["MAP"] < 60:
            steps_taken.append(15)  # GiveFluids
            continue

        if vitals.get("HeartRate") is not None:
            if vitals["HeartRate"] < 50:
                steps_taken.append(12)  # GiveAtropine
                continue
            elif vitals["HeartRate"] > 150:
                steps_taken.append(9)  # GiveAdenosine
                continue
        
        if (events[27]):  # HeartRhythmNSR
            steps_taken.append(24)  # UseMonitorPads

        steps_taken.append(48)  # Finish
        break

    for action in steps_taken:
        print(action)

if __name__ == "__main__":
    main()
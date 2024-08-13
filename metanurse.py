import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
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
                    "Resps"
                ],
            )
        }

        if step == 0:
            print(3)  # ExamineAirway
            continue
        
        if "sats_probe" not in actions_taken:
            print(25)  # UseSatsProbe
            actions_taken.add("sats_probe")
            continue

        if "bp_cuff" not in actions_taken:
            print(27)  # UseBloodPressureCuff
            actions_taken.add("bp_cuff")
            continue

        if "view_monitor" not in actions_taken:
            print(16)  # ViewMonitor
            actions_taken.add("view_monitor")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue
        
        if vitals["HeartRate"] is not None and vitals["HeartRate"] > 150:
            print(43)  # DefibrillatorPace
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue
        
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(0)  # DoNothing to continue the loop if no action needed

if __name__ == "__main__":
    stabilize()
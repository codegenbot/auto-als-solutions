import sys

def stabilize():
    max_steps = 350
    action_taken = { "examine": False, "sats_probe": False, "view_monitor": False, "bp_cuff": False }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times, [
                    "HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                    "MAP", "Sats", "Resps"
                ]
            )
        }

        if not action_taken["examine"]:
            action_taken["examine"] = True
            print(3)  # ExamineAirway
            continue

        if not action_taken["sats_probe"]:
            print(25)  # UseSatsProbe
            action_taken["sats_probe"] = True
            continue

        if not action_taken["view_monitor"]:
            print(16)  # ViewMonitor
            action_taken["view_monitor"] = True
            continue

        if not action_taken["bp_cuff"]:
            print(27)  # UseBloodPressureCuff
            action_taken["bp_cuff"] = True
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        is_unstable_tach = (vitals["HeartRate"] is not None and vitals["HeartRate"] > 150) or events[32] > 0
        if is_unstable_tach:
            print(40)  # DefibrillatorCharge
            continue

        if all( vital is not None and vital >= threshold for vital, threshold in zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]) ):
            print(48)  # Finish
            return
        
        print(15)  # Default to giving fluids if no critical action required

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    max_steps = 350
    actions_taken = {
        "sats_probe": False,
        "bp_cuff": False,
        "view_monitor": False,
        "airway": False,
        "breathing": False,
        "circulation": False,
        "disability": False,
        "exposure": False
    }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )
        vitals = {
            name: value if time != 0.0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                 "MAP", "Sats", "Resps"]
            )
        }

        # Initial necessary examinations
        if not actions_taken["sats_probe"]:
            actions_taken["sats_probe"] = True
            print(25)  # UseSatsProbe
            continue
        if not actions_taken["bp_cuff"]:
            actions_taken["bp_cuff"] = True
            print(27)  # UseBloodPressureCuff
            continue
        if not actions_taken["view_monitor"]:
            actions_taken["view_monitor"] = True
            print(16)  # ViewMonitor
            continue

        # ABCDE Assessments
        if not actions_taken["airway"]:
            actions_taken["airway"] = True
            print(3)  # ExamineAirway
            continue
        if not actions_taken["breathing"]:
            actions_taken["breathing"] = True
            print(4)  # ExamineBreathing
            continue
        if not actions_taken["circulation"]:
            actions_taken["circulation"] = True
            print(5)  # ExamineCirculation
            continue

        # Check for critical interventions
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
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

        # Stabilization check
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(0)  # DoNothing if no immediate action

if __name__ == "__main__":
    stabilize()
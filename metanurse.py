import sys

def stabilize():
    max_steps = 350
    state = {
        "first_examine": False,
        "use_sats_probe": False,
        "use_blood_pressure_cuff": False,
        "view_monitor": False,
    }

    def initial_steps(step):
        if step == 0 or not state["first_examine"]:
            state["first_examine"] = True
            return 3  # ExamineAirway
        if not state["use_sats_probe"]:
            state["use_sats_probe"] = True
            return 25  # UseSatsProbe
        if not state["use_blood_pressure_cuff"]:
            state["use_blood_pressure_cuff"] = True
            return 27  # UseBloodPressureCuff
        if not state["view_monitor"]:
            state["view_monitor"] = True
            return 16  # ViewMonitor
        return None

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

        action = initial_steps(step)
        if action is not None:
            print(action)
            continue

        # Check critical conditions and respond
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["HeartRate"] is not None and (
            vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50
        ):
            print(24)  # UseMonitorPads
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

    print(48)  # Ensure the game ends after max steps

if __name__ == "__main__":
    stabilize()
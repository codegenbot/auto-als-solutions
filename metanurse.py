import sys

def stabilize():
    max_steps = 350
    initial_examine = True
    use_sats_probe = use_blood_pressure_cuff = view_monitor = False
    actions = iter([3, 4, 3, 8, 16])  # Initial series of Examine actions

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

        # Initial examinations
        if initial_examine:
            try:
                print(next(actions))
                continue
            except StopIteration:
                initial_examine = False

        # Use Sats Probe
        if not use_sats_probe:
            print(25)
            use_sats_probe = True
            continue

        # Use Blood Pressure Cuff
        if not use_blood_pressure_cuff:
            print(27)
            use_blood_pressure_cuff = True
            continue

        # View Monitor
        if not view_monitor:
            print(16)
            view_monitor = True
            continue

        # Check for immediate critical interventions
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # Start CPR
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # Start CPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # Use Non-Rebreather Mask
            continue
            
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue
            
        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            print(24)  # Use Monitor Pads
            continue

        # Finish if patient is stabilized
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return
        
        # Default action if nothing else is triggered
        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()
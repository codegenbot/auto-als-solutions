import sys


def stabilize():
    max_steps = 350
    examined = {"airway": False, "breathing": False, "circulation": False}
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

        if not examined["airway"]:
            examined["airway"] = True
            print(3)  # Examine Airway
            continue
        elif not examined["breathing"]:
            examined["breathing"] = True
            print(4)  # Examine Breathing
            continue
        elif not examined["circulation"]:
            examined["circulation"] = True
            print(5)  # Examine Circulation
            continue
        elif "MAP" not in vitals or vitals["MAP"] is None:
            print(27)  # Use Blood Pressure Cuff
            continue
        elif "Sats" not in vitals or vitals["Sats"] is None:
            print(25)  # Use Sats Probe
            continue
        elif not vital_signs_times[6]:  # Check for MAP and Sats measured together
            print(16)  # View Monitor
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            print(17)  # Start Chest Compression
            continue
        if vitals["HeartRate"] is not None and vitals["HeartRate"] > 150:
            print(24)  # Use Monitor Pads
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # Give Fluids
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # Use Non Rebreather Mask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(48)  # Finish
        return


if __name__ == "__main__":
    stabilize()
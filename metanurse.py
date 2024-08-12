import sys

def main():
    max_steps = 350
    used_methods = {
        "UsedSatsProbe": False,
        "ViewedMonitor": False,
        "OpenedBreathingDrawer": False,
        "OpenedCirculationDrawer": False,
        "BP_CuffOn": False,
        "GivenFluids": False,
        "GivenAtropine": False,
    }

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
                (
                    "HeartRate",
                    "RespRate",
                    "CapillaryGlucose",
                    "Temperature",
                    "MAP",
                    "Sats",
                    "Resps",
                ),
            )
        }

        if not events[3]:
            print(3)  # Examine Airway
            continue

        if not used_methods["OpenedBreathingDrawer"]:
            print(19)  # Open Breathing Drawer
            used_methods["OpenedBreathingDrawer"] = True
            continue

        if not used_methods["UsedSatsProbe"]:
            print(25)  # Use Sats Probe
            used_methods["UsedSatsProbe"] = True
            continue

        if not used_methods["ViewedMonitor"]:
            print(16)  # View Monitor
            used_methods["ViewedMonitor"] = True
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # Start Chest Compression
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_methods["OpenedCirculationDrawer"]:
                print(20)  # Open Circulation Drawer
                used_methods["OpenedCirculationDrawer"] = True
            elif not used_methods["GivenFluids"]:
                print(15)  # Give Fluids
                used_methods["GivenFluids"] = True
            continue

        if vitals["HeartRate"] and vitals["HeartRate"] > 150:
            print(2)  # Check Rhythm (Cardioversion)
            continue

        if vitals["HeartRate"] and vitals["HeartRate"] < 50:
            if not used_methods["GivenAtropine"]:
                print(12)  # Give Atropine
                used_methods["GivenAtropine"] = True
            continue

        print(48)  # Finish
        return

    print(48)  # Finish

if __name__ == "__main__":
    main()
import sys

def main():
    max_steps = 350
    used_methods = {
        "UsedSatsProbe": False,
        "ViewedMonitor": False,
        "OpenedBreathingDrawer": False,
        "OpenedCirculationDrawer": False,
        "UsedBP_Cuff": False,
        "GivenFluids": False,
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

        # Check for immediate life-threatening conditions.
        if vitals["Sats"] and vitals["Sats"] < 65:
            print(17)  # StartChestCompression for cardiac arrest
            continue
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # StartChestCompression for cardiac arrest
            continue

        # Perform Airway Assessment
        if not events[3]:  # AirwayClear
            print(3)  # ExamineAirway
            continue

        # Open necessary drawers and use probes
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

        # Check vital signs and apply treatments
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use Non-Rebreather Mask
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use Bag-Valve-Mask
            continue
        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_methods["OpenedCirculationDrawer"]:
                print(20)  # Open Circulation Drawer
                used_methods["OpenedCirculationDrawer"] = True
                continue
            if not used_methods["UsedBP_Cuff"]:
                print(27)  # Use Blood Pressure Cuff
                used_methods["UsedBP_Cuff"] = True
                continue
            if not used_methods["GivenFluids"]:
                print(15)  # Give Fluids
                used_methods["GivenFluids"] = True
                continue

        # Handle Heart Rate conditions
        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)  # Give Atropine
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(2)  # CheckRhythm
                continue
            elif vitals["HeartRate"] > 150:
                print(40)  # DefibrillatorCharge (for cardioversion)
                continue

        print(48)  # Finish when stabilized
        return

    print(48)  # Finish

if __name__ == "__main__":
    main()
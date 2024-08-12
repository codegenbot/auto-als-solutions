import sys

def main():
    max_steps = 350
    used_methods = {
        "OpenedBreathingDrawer": False,
        "UsedSatsProbe": False,
        "ViewedMonitor": False,
        "OpenedCirculationDrawer": False,
        "UsedMonitorPads": False,
        "BP_CuffOn": False,
        "UsedA_Line": False,
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
                ("HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"),
            )
        }

        # Check Airway
        if not events[3]:
            print(3)  # Examine Airway
            continue
        
        # Open Breathing Drawer
        if not used_methods["OpenedBreathingDrawer"]:
            print(19)  # Open Breathing Drawer
            used_methods["OpenedBreathingDrawer"] = True
            continue

        # Use Sats Probe
        if not used_methods["UsedSatsProbe"]:
            print(25)  # Use Sats Probe
            used_methods["UsedSatsProbe"] = True
            continue

        # View Monitor
        if not used_methods["ViewedMonitor"]:
            print(16)  # View Monitor
            used_methods["ViewedMonitor"] = True
            continue
        
        # Handle Breathing Issues
        if vitals["Sats"] and vitals["Sats"] < 65:
            print(17)  # Start Chest Compression
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue
        
        # Ensure MAP is sufficient
        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_methods["OpenedCirculationDrawer"]:
                print(20)  # Open Circulation Drawer
                used_methods["OpenedCirculationDrawer"] = True
                continue
            if not used_methods["UsedMonitorPads"]:
                print(24)  # Use Monitor Pads
                used_methods["UsedMonitorPads"] = True
                continue
            if not used_methods["BP_CuffOn"]:
                print(27)  # Use Blood Pressure Cuff
                used_methods["BP_CuffOn"] = True
                continue
            if not used_methods["UsedA_Line"]:
                print(26)  # Use A-Line
                used_methods["UsedA_Line"] = True
                continue
            if not used_methods["GivenFluids"]:
                print(15)  # Give Fluids
                used_methods["GivenFluids"] = True
                continue
        
        # Handle Heart Rate Issues
        if vitals["HeartRate"] and vitals["HeartRate"] > 150:
            if vitals["MAP"] and vitals["MAP"] < 60:
                print(2)  # Check Rhythm (for Cardioversion)
            else:
                print(9)  # Give Adenosine
            continue

        if vitals["HeartRate"] and vitals["HeartRate"] < 50:
            print(12)  # Give Atropine
            continue
        
        # If all vitals are stabilised, finish
        if (events[3] and
            (vitals["Sats"] is None or vitals["Sats"] >= 88) and
            (vitals["RespRate"] is None or vitals["RespRate"] >= 8) and
            (vitals["MAP"] is None or vitals["MAP"] >= 60)):
            print(48)  # Finish
            return

    print(48)  # Finish

if __name__ == "__main__":
    main()
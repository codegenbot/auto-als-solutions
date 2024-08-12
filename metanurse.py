import sys

def main():
    max_steps = 350
    used_methods = {
        "UsedSatsProbe": False,
        "ViewedMonitor": False,
        "OpenedBreathingDrawer": False,
        "OpenedCirculationDrawer": False,
        "UsedMonitorPads": False,
        "UsedBP_Cuff": False,
        "UsedA_Line": False,
        "GivenFluids": False,
    }

    def is_stable(vitals):
        return (vitals["Sats"] and vitals["Sats"] >= 88 and
                vitals["RespRate"] and vitals["RespRate"] >= 8 and
                vitals["MAP"] and vitals["MAP"] >= 60)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vitals_times, vitals_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vitals_values,
                vitals_times,
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

        # Check and update airway
        if not events[3]:  # AirwayClear
            print(3)
            continue

        # Open breathing drawer and use necessary tools
        if not used_methods["OpenedBreathingDrawer"]:
            print(19)
            used_methods["OpenedBreathingDrawer"] = True
            continue

        if not used_methods["UsedSatsProbe"]:
            print(25)
            used_methods["UsedSatsProbe"] = True
            continue

        if not used_methods["ViewedMonitor"]:
            print(16)
            used_methods["ViewedMonitor"] = True
            continue

        # Check for cardiac arrest conditions
        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20):
            print(17)
            continue

        # Stabilize by providing oxygen or ventilation support
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue

        # Handle blood pressure issues
        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_methods["OpenedCirculationDrawer"]:
                print(20)
                used_methods["OpenedCirculationDrawer"] = True
            elif not used_methods["UsedMonitorPads"]:
                print(24)
                used_methods["UsedMonitorPads"] = True
            elif not used_methods["UsedBP_Cuff"]:
                print(27)
                used_methods["UsedBP_Cuff"] = True
            elif not used_methods["UsedA_Line"]:
                print(26)
                used_methods["UsedA_Line"] = True
            elif not used_methods["GivenFluids"]:
                print(15)
                used_methods["GivenFluids"] = True
            continue

        # Check and handle tachyarrhythmia
        if vitals["HeartRate"] and vitals["HeartRate"] > 150:
            if vitals["MAP"] and vitals["MAP"] < 60:  # unstable
                print(17)  # Cardioversion would be an option, for demo CPR
                continue
            print(2)
            continue

        # Check for high heart rate
        if vitals["HeartRate"] and vitals["HeartRate"] > 100:
            print(9)
            continue

        # If stabilized, finish
        if is_stable(vitals):
            print(48)
            return

    print(48)

if __name__ == "__main__":
    main()
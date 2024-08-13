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
        "UsedDefibPads": False,
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

        if not events[3]:
            print(3)  # ExamineAirway
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue
        
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_methods["OpenedCirculationDrawer"]:
                print(20)  # OpenCirculationDrawer
                used_methods["OpenedCirculationDrawer"] = True
            elif not used_methods["UsedMonitorPads"]:
                print(24)  # UseMonitorPads
                used_methods["UsedMonitorPads"] = True
            elif not used_methods["UsedBP_Cuff"]:
                print(27)  # UseBloodPressureCuff
                used_methods["UsedBP_Cuff"] = True
            elif not used_methods["UsedA_Line"]:
                print(26)  # UseAline
                used_methods["UsedA_Line"] = True
            elif not used_methods["GivenFluids"]:
                print(15)  # GiveFluids
                used_methods["GivenFluids"] = True
            continue

        if not used_methods["OpenedBreathingDrawer"]:
            print(19)  # OpenBreathingDrawer
            used_methods["OpenedBreathingDrawer"] = True
            continue

        if not used_methods["UsedSatsProbe"]:
            print(25)  # UseSatsProbe
            used_methods["UsedSatsProbe"] = True
            continue

        if not used_methods["ViewedMonitor"]:
            print(16)  # ViewMonitor
            used_methods["ViewedMonitor"] = True
            continue

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)  # GiveAtropine
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(2)  # CheckRhythm
                continue
            elif vitals["HeartRate"] > 150:
                print(40)  # DefibrillatorCharge
                continue

        print(48)  # Finish
        return

    print(48)  # Finish

if __name__ == "__main__":
    main()
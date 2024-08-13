import sys

def main():
    max_steps = 350
    used_methods = {
        "UsedSatsProbe": False,
        "ViewedMonitor": False,
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

        # **Airway check**
        if not events[3]:
            print(3)
            continue
        
        # **Breathing check**
        if not used_methods["UsedSatsProbe"]:
            print(25)
            used_methods["UsedSatsProbe"] = True
            continue

        if not used_methods["ViewedMonitor"]:
            print(16)
            used_methods["ViewedMonitor"] = True
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            print(17)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue
        
        # **Circulation check**
        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_methods["OpenedCirculationDrawer"]:
                print(20)
                used_methods["OpenedCirculationDrawer"] = True
            elif not used_methods["UsedBP_Cuff"]:
                print(27)
                used_methods["UsedBP_Cuff"] = True
            elif not used_methods["GivenFluids"]:
                print(15)
                used_methods["GivenFluids"] = True
            continue

        # **Defibrillation for critical HeartRate values**
        if vitals["HeartRate"]:
            if vitals["HeartRate"] > 150:
                print(28)
                continue
        
        print(48)
        return

    print(48)

if __name__ == "__main__":
    main()
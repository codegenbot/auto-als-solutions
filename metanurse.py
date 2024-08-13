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
        "DefibrillatorCharged": False,
    }

    steps = {
        "examine_airway": False,
        "open_breathing_drawer": False,
        "use_sats_probe": False,
        "view_monitor": False,
        "open_circulation_drawer": False,
        "use_monitor_pads": False,
        "use_bp_cuff": False,
        "use_a_line": False,
        "give_fluids": False,
        "use_defib_pads": False,
        "defibrillator_charged": False,
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

        # Airway
        if not steps["examine_airway"]:
            print(3)
            steps["examine_airway"] = True
            continue

        if events[3]:
            steps["examine_airway"] = True

        # Breathing
        if not steps["open_breathing_drawer"]:
            print(19)
            steps["open_breathing_drawer"] = True
            continue

        if not steps["use_sats_probe"]:
            print(25)
            steps["use_sats_probe"] = True
            continue

        # Circulation
        if not steps["view_monitor"]:
            print(16)
            steps["view_monitor"] = True
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

        if vitals["MAP"] and vitals["MAP"] < 60:
            if not steps["open_circulation_drawer"]:
                print(20)
                steps["open_circulation_drawer"] = True
            elif not steps["use_monitor_pads"]:
                print(24)
                steps["use_monitor_pads"] = True
            elif not steps["use_bp_cuff"]:
                print(27)
                steps["use_bp_cuff"] = True
            elif not steps["use_a_line"]:
                print(26)
                steps["use_a_line"] = True
            elif not steps["give_fluids"]:
                print(15)
                steps["give_fluids"] = True
            continue

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(2)
                continue
            elif vitals["HeartRate"] > 150:
                if not steps["use_defib_pads"]:
                    print(28)
                    steps["use_defib_pads"] = True
                    continue
                if not steps["defibrillator_charged"]:
                    print(40)
                    steps["defibrillator_charged"] = True
                    continue
                print(44)
                continue

        print(48)
        return

    print(48)

if __name__ == "__main__":
    main()
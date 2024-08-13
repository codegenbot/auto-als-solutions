import sys


def main():
    max_steps = 350
    steps_left = max_steps
    initialized = False
    used_methods = {
        "UsedSatsProbe": False,
        "UsedBP_Cuff": False,
        "UsedA_Line": False,
        "GivenFluids": False,
        "OpenedBreathingDrawer": False,
        "ViewedMonitor": False,
        "OpenedCirculationDrawer": False,
        "UsedMonitorPads": False,
        "OpenedAirwayDrawer": False,
    }

    while steps_left > 0:
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "CapillaryGlucose": vital_signs_values[2]
            if vital_signs_times[2] > 0
            else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
            "Resps": vital_signs_values[6] if vital_signs_times[6] > 0 else None,
        }

        steps_left -= 1

        if not initialized:
            print(3)  # ExamineAirway
            initialized = True
            continue

        if vitals["Sats"] is None:
            if not used_methods["UsedSatsProbe"]:
                print(25)  # UseSatsProbe
                used_methods["UsedSatsProbe"] = True
                continue
            if not used_methods["ViewedMonitor"]:
                print(16)  # ViewMonitor
                used_methods["ViewedMonitor"] = True
                continue
        elif vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is None:
            print(4)  # ExamineBreathing
            continue
        elif vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is None:
            if not used_methods["UsedBP_Cuff"]:
                print(27)  # UseBloodPressureCuff
                used_methods["UsedBP_Cuff"] = True
                continue
            if not used_methods["ViewedMonitor"]:
                print(16)  # ViewMonitor
                used_methods["ViewedMonitor"] = True
                continue
        elif vitals["MAP"] < 60:
            if not used_methods["OpenedCirculationDrawer"]:
                print(20)  # OpenCirculationDrawer
                used_methods["OpenedCirculationDrawer"] = True
                continue
            if not used_methods["UsedMonitorPads"]:
                print(24)  # UseMonitorPads
                used_methods["UsedMonitorPads"] = True
                continue
            if not used_methods["UsedA_Line"]:
                print(26)  # UseAline
                used_methods["UsedA_Line"] = True
                continue
            if not used_methods["GivenFluids"]:
                print(15)  # GiveFluids
                used_methods["GivenFluids"] = True
                continue

        if vitals["HeartRate"] is None:
            print(6)  # ExamineCirculation
            continue
        elif vitals["HeartRate"] < 50:
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

    print(48)  # Finish if max_steps reached


if __name__ == "__main__":
    main()
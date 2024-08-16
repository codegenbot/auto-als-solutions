import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def examine_or_measure():
        checks = ["ExamineAirway", "ExamineBreathing", "ExamineCirculation", "ExamineDisability", "ExamineExposure"]
        if not all(check in examined for check in checks):
            for check in checks:
                if check not in examined:
                    action_map = {
                        "ExamineAirway": 3, "ExamineBreathing": 4,
                        "ExamineCirculation": 5, "ExamineDisability": 6,
                        "ExamineExposure": 7
                    }
                    take_action(action_map[check])
                    examined.add(check)
                    return

        vital_checks = ["Monitor", "BP", "SatsProbe"]
        if not all(check in examined for check in vital_checks):
            for check in vital_checks:
                if check not in examined:
                    action_map = {"Monitor": 16, "BP": 27, "SatsProbe": 25}
                    take_action(action_map[check])
                    examined.add(check)
                    return
    
    examined = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {"HR": values[0] if times[0] > 0 else None,
                  "RR": values[1] if times[1] > 0 else None,
                  "Glucose": values[2] if times[2] > 0 else None,
                  "Temp": values[3] if times[3] > 0 else None,
                  "MAP": values[4] if times[4] > 0 else None,
                  "Sats": values[5] if times[5] > 0 else None,
                  "Resps": values[6] if times[6] > 0 else None}

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue
        
        examine_or_measure()

        if vitals["MAP"] and vitals["MAP"] < 60:
            if "CirculationDrawer" not in examined:
                take_action(20)  # OpenCirculationDrawer
                examined.add("CirculationDrawer")
                continue
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            if "BreathingDrawer" not in examined:
                take_action(19)  # OpenBreathingDrawer
                examined.add("BreathingDrawer")
                continue
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["HR"] and (vitals["HR"] > 150):
            if "DrugsDrawer" not in examined:
                take_action(21)  # OpenDrugsDrawer
                examined.add("DrugsDrawer")
                continue
            take_action(24)  # UseMonitorPads for cardioversion
            continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
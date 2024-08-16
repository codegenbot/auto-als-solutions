import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    vitals_checked = {"Sats": False, "RR": False, "MAP": False, "HR": False, "ViewMonitor": False}
    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue
            
        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]
        
        vitals = {
            "HR": values[0] if times[0] != 0 else None,
            "RR": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }
        
        # Check vitals for immediate cardiac arrest conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue
        
        if vitals["Sats"] is None and not vitals_checked["Sats"]:
            take_action(25)  # UseSatsProbe
            vitals_checked["Sats"] = True
            continue

        if vitals["RR"] is None and not vitals_checked["RR"]:
            take_action(4)  # ExamineBreathing
            vitals_checked["RR"] = True
            continue
        
        if vitals["MAP"] is None and not vitals_checked["MAP"]:
            take_action(27)  # UseBloodPressureCuff
            vitals_checked["MAP"] = True
            continue
        
        if vitals["HR"] is None and not vitals_checked["HR"]:
            take_action(24)  # UseMonitorPads
            vitals_checked["HR"] = True
            continue
        
        if not vitals_checked["ViewMonitor"]:
            take_action(16)  # ViewMonitor
            vitals_checked["ViewMonitor"] = True
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
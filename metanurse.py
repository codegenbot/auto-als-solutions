import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    
    def examine_vitals():
        if "BreathingDrawer" not in examined:
            take_action(19)  # OpenBreathingDrawer
            examined.add("BreathingDrawer")
            return
        if "Monitor" not in examined:
            take_action(16)  # ViewMonitor
            examined.add("Monitor")
            return
        if "SatsProbe" not in examined:
            take_action(25)  # UseSatsProbe
            examined.add("SatsProbe")
            return
        if "BP" not in examined:
            take_action(27)  # UseBloodPressureCuff
            examined.add("BP")
            return

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] else None,
            "RR": values[1] if times[1] else None,
            "Glucose": values[2] if times[2] else None,
            "Temp": values[3] if times[3] else None,
            "MAP": values[4] if times[4] else None,
            "Sats": values[5] if times[5] else None,
            "Resps": values[6] if times[6] else None
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if events[3] == 0 and "Airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("Airway")
            continue
        
        if events[9] == 0 and "Breathing" not in examined:
            take_action(4)  # ExamineBreathing
            examined.add("Breathing")
            continue

        examine_vitals()

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["HR"] is not None:
            if vitals["HR"] > 150:
                take_action(9)  # GiveAdenosine
                continue
            elif vitals["HR"] > 100:
                take_action(24)  # UseMonitorPads
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # GiveAtropine
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
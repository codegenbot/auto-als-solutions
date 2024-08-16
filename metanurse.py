import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()
    
    actions = {
        "ViewMonitor": 16,
        "UseSatsProbe": 25,
        "TakeBloodPressure": 38,
        "ExamineAirway": 3,
        "ExamineBreathing": 4,
        "ExamineCirculation": 5,
        "GiveFluids": 15,
        "UseNonRebreatherMask": 30,
        "UseBagValveMask": 29,
        "UseMonitorPads": 24,
        "GiveAdenosine": 9,
        "GiveAtropine": 12,
        "OpenBreathingDrawer": 19,
        "OpenCirculationDrawer": 20,
        "StartChestCompression": 17,
        "Finish": 48
    }

    examined = set()
    drawer_opened = set()
    
    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue
        
        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(actions["StartChestCompression"])
            continue

        if "Airway" not in examined:
            take_action(actions["ExamineAirway"])
            examined.add("Airway")
            if events[3] > 0:
                examined.add("Breathing")
                examined.add("Circulation")
            continue

        if "Breathing" not in examined:
            take_action(actions["ExamineBreathing"])
            examined.add("Breathing")
            if events[33] == 0 and "BreathingDrawer" not in drawer_opened:
                take_action(actions["OpenBreathingDrawer"])
                drawer_opened.add("BreathingDrawer")
            continue

        if "Circulation" not in examined:
            take_action(actions["ExamineCirculation"])
            examined.add("Circulation")
            if events[36] == 0 and "CirculationDrawer" not in drawer_opened:
                take_action(actions["OpenCirculationDrawer"])
                drawer_opened.add("CirculationDrawer")
            continue

        if "Monitor" not in examined:
            take_action(actions["ViewMonitor"])
            examined.add("Monitor")
            continue

        if "SatsProbe" not in examined:
            take_action(actions["UseSatsProbe"])
            examined.add("SatsProbe")
            continue

        if "BP" not in examined:
            take_action(actions["TakeBloodPressure"])
            examined.add("BP")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(actions["GiveFluids"])
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(actions["UseNonRebreatherMask"])
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(actions["UseBagValveMask"])
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(actions["UseMonitorPads"])
                continue
            elif vitals["HR"] > 100:
                take_action(actions["GiveAdenosine"])
                continue
            elif vitals["HR"] < 50:
                take_action(actions["GiveAtropine"])
                continue

        take_action(actions["Finish"])
        break
    else:
        take_action(actions["Finish"])

if __name__ == "__main__":
    stabilize()
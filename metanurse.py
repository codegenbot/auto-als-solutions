import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    actions = {
        "airway": 3, 
        "breathing": 4, 
        "circulation": 5, 
        "disability": 6, 
        "exposure": 7, 
        "monitor": 16,
        "BP_cuff": 27,
        "sats_probe": 25,
        "finish": 48
    }

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
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start CPR
            continue
        
        if "monitor" not in examined_vitals:
            take_action(actions["monitor"])
            examined_vitals.add("monitor")
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(actions["BP_cuff"])
            examined_vitals.add("MAP")
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(actions["sats_probe"])
            examined_vitals.add("Sats")
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(actions["breathing"])
            examined_vitals.add("RR")
            continue

        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(actions["airway"])
            examined_vitals.add("airway")
            continue

        if any(events[i] > 0 for i in range(7, 15)) and "breathing" not in examined_vitals:
            take_action(actions["breathing"])
            examined_vitals.add("breathing")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30 if "mask" not in examined_vitals else 29)
            examined_vitals.add("mask")
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask
            continue
        
        if vitals["HR"] is not None and any(events[i] > 0 for i in range(30, 33)):
            take_action(43)  # DefibrillatorPace
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(actions["exposure"])
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(actions["circulation"])
            examined_vitals.add("circulation")
            continue

        if step > 300:
            take_action(actions["finish"])
            break

if __name__ == "__main__":
    stabilize()
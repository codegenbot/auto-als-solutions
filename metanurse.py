import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()
    checked_vitals = {"HR": False, "MAP": False, "Sats": False}
    
    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        vitals_time = observations[33:40]
        measurements = observations[46:]

        vitals = {
            "HR": measurements[0] if vitals_time[0] > 0 else None,
            "RR": measurements[1] if vitals_time[1] > 0 else None,
            "Glucose": measurements[2] if vitals_time[2] > 0 else None,
            "Temp": measurements[3] if vitals_time[3] > 0 else None,
            "MAP": measurements[4] if vitals_time[4] > 0 else None,
            "Sats": measurements[5] if vitals_time[5] > 0 else None,
            "Resps": measurements[6] if vitals_time[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue
        
        if all(events[i] == 0 for i in range(3, 7)) and "Airway" not in examined:
            take_action(3)  # Examine Airway
            examined.add("Airway")
            continue
        
        if not checked_vitals["Sats"] and vitals["Sats"] is None:
            take_action(25)  # Use Sats Probe
            checked_vitals["Sats"] = True
            continue
        
        if not checked_vitals["MAP"] and vitals["MAP"] is None:
            take_action(27)  # Use Blood Pressure Cuff
            checked_vitals["MAP"] = True
            continue
        
        if "Breathing" not in examined and any(events[i] > 0 for i in (3, 4, 5, 6)):
            take_action(4)  # Examine Breathing
            examined.add("Breathing")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if not checked_vitals["HR"] and vitals["HR"] is None:
            take_action(16)  # View Monitor
            checked_vitals["HR"] = True
            continue

        if vitals["HR"] is not None:
            if vitals["HR"] > 150:
                take_action(24)  # Use Monitor Pads (for cardioversion)
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # Give Atropine
                continue
            elif vitals["HR"] > 100:
                take_action(9)  # Give Adenosine
                continue
        
        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        last_measured = observations[33:40]
        values = observations[46:]

        vitals = {
            "HR": values[0] if observations[40] > 0 else None,
            "RR": values[1] if observations[41] > 0 else None,
            "Glucose": values[2] if observations[42] > 0 else None,
            "Temp": values[3] if observations[43] > 0 else None,
            "MAP": values[4] if observations[44] > 0 else None,
            "Sats": values[5] if observations[45] > 0 else None,
            "Resps": values[6] if observations[46] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        # Airway check (Examine Airway if never examined)
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # Examine Airway
            examined.add("Airway")
            continue

        if events[3]:  # AirwayClear
            if any(events[7:15]) and "Breathing" not in examined:
                take_action(4)  # Examine Breathing
                examined.add("Breathing")
                continue

        if "Sats" not in examined and vitals["Sats"] is None:
            take_action(25)  # Use Sats Probe
            examined.add("Sats")
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if "MAP" not in examined and vitals["MAP"] is None:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("MAP")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if "Circulation" not in examined:
            take_action(5)  # Examine Circulation
            examined.add("Circulation")
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if any(events[i] for i in range(28, 33)):  # Heart arrhythmia events 
            take_action(24)  # Use Monitor Pads (for defibrillation/cardioversion)
            continue

        if vitals["HR"]:
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
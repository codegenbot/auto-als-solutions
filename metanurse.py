import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

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
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start Chest Compression
            continue

        if "monitor" not in examined_vitals:
            take_action(16)  # View Monitor
            examined_vitals.add("monitor")
            continue

        if vitals["MAP"] is None and "BP" not in examined_vitals:
            take_action(27)  # Use Blood Pressure Cuff
            examined_vitals.add("BP")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is None and "SatsProbe" not in examined_vitals:
            take_action(25)  # Use Sats Probe
            examined_vitals.add("SatsProbe")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            action = 30 if 30 not in examined_vitals else 29
            take_action(action)  # Use Non Rebreather Mask or Use Bag Valve Mask
            examined_vitals.add(action)
            continue

        if vitals["RR"] is None and "Breathing" not in examined_vitals:
            take_action(4)  # Examine Breathing
            examined_vitals.add("Breathing")
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if any(events[i] > 0 for i in range(28, 33)):  # Check for arrhythmias
            if any(events[i] > 0 for i in [31, 32]):  # If VT or VF
                take_action(10)  # Give Adrenaline
            elif any(events[i] > 0 for i in [29, 30]):  # If SVT or Atrial Flutter
                take_action(9)  # Give Adenosine
            else:
                take_action(2)  # Check Rhythm
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
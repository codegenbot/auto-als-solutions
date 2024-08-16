import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    handled_airway = False
    handled_breathing = False
    handled_circulation = False
    examined = set()

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

        # Cardiac Arrest Check
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compressions
            continue

        # Airway Assessment
        if not handled_airway:
            if "airway" not in examined:
                take_action(3)  # Examine airway
                examined.add("airway")
                continue
            
            if any(events[i] > 0 for i in [4, 5, 6]):  # Vomit, Blood, Tongue
                take_action(35)  # Perform airway manoeuvres
                continue
            
            handled_airway = True

        # Breathing Assessment
        if not handled_breathing:
            if "SatsProbe" not in examined:
                take_action(25)  # Use SatsProbe
                examined.add("SatsProbe")
                continue

            if "Breathing" not in examined:
                take_action(4)  # Examine breathing
                examined.add("Breathing")
                continue

            if vitals["Sats"] is not None and vitals["Sats"] < 88:
                take_action(30)  # UseNonRebreatherMask
                continue

            if vitals["RR"] is not None and vitals["RR"] < 8:
                take_action(29)  # Use Bag Valve Mask
                continue
            
            handled_breathing = True
        
        # Circulation Assessment
        if not handled_circulation:
            if "BP" not in examined:
                take_action(27)  # Use Blood Pressure Cuff
                examined.add("BP")
                continue

            if "Monitor" not in examined:
                take_action(16)  # View Monitor
                examined.add("Monitor")
                continue

            if vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(15)  # Give Fluids
                continue

            handled_circulation = True

        # If all assessments are handled and vitals are stable, finish
        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
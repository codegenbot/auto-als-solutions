import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    
    def examine_vitals():
        if "Monitor" not in examined:
            take_action(16)  # View Monitor
            examined.add("Monitor")
            return
        if "SatsProbe" not in examined:
            take_action(25)  # Use Sats Probe
            examined.add("SatsProbe")
            return
        if "BPCuff" not in examined:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("BPCuff")
            return

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        values = observations[46:]

        vitals = {
            "HR": values[0] if observations[33] > 0 else None,
            "RR": values[1] if observations[34] > 0 else None,
            "Glucose": values[2] if observations[35] > 0 else None,
            "Temp": values[3] if observations[36] > 0 else None,
            "MAP": values[4] if observations[37] > 0 else None,
            "Sats": values[5] if observations[38] > 0 else None,
            "Resps": values[6] if observations[39] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # Examine Airway
            examined.add("Airway")
            continue

        if events[3]:
            if not any(events[7:15]) and "Breathing" not in examined:
                take_action(4)  # Examine Breathing
                examined.add("Breathing")
                continue
            if events[8]:  # BreathingSnoring
                take_action(36)  # Perform Head Tilt Chin Lift
                continue

        examine_vitals()

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if any(events[i] for i in range(28, 33)):  # Heart arrhythmia events
            take_action(24)  # Use Monitor Pads (for defibrillation)
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)  # Use Monitor Pads (for cardioversion)
                continue
            elif vitals["HR"] > 100:
                take_action(9)  # Give Adenosine
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # Give Atropine
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
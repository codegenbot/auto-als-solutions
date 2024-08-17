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
        measurement_time = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if measurement_time[0] else None,
            "RR": measurements[1] if measurement_time[1] else None,
            "Glucose": measurements[2] if measurement_time[2] else None,
            "Temp": measurements[3] if measurement_time[3] else None,
            "MAP": measurements[4] if measurement_time[4] else None,
            "Sats": measurements[5] if measurement_time[5] else None,
            "Resps": measurements[6] if measurement_time[6] else None,
        }

        # Check for immediate cardiac arrest risk
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        # ABCDE Assessment
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # Examine Airway
            examined.add("Airway")
            continue
        
        if events[3]:  # AirwayClear
            if events[8]:  # BreathingSnoring
                take_action(36)  # Perform Head Tilt Chin Lift
                continue
            if not any(events[7:15]) and "Breathing" not in examined:
                take_action(4)  # Examine Breathing
                examined.add("Breathing")
                continue

        if not any([events[9], events[10], events[12], events[13], events[14]]) and "BreathingTreatment" not in examined:
            take_action(19)  # OpenBreathingDrawer
            examined.add("BreathingTreatment")
            continue

        if "Sats" not in examined:
            take_action(25)  # Use Sats Probe
            examined.add("Sats")
            continue

        if "MAP" not in examined:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("MAP")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if vitals["HR"] is not None:
            if vitals["HR"] > 150 or vitals["HR"] < 50:
                take_action(24)  # Use Monitor Pads (for cardioversion)
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
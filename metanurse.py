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
        measurement_times = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if measurement_times[0] else None,
            "RR": measurements[1] if measurement_times[1] else None,
            "Glucose": measurements[2] if measurement_times[2] else None,
            "Temp": measurements[3] if measurement_times[3] else None,
            "MAP": measurements[4] if measurement_times[4] else None,
            "Sats": measurements[5] if measurement_times[5] else None,
            "Resps": measurements[6] if measurement_times[6] else None,
        }

        # Check for immediate critical conditions
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        # Airway Assessment
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # Examine Airway
            examined.add("Airway")
            continue

        # Breathing Assessment
        if "Breathing" not in examined:
            take_action(4)  # Examine Breathing
            examined.add("Breathing")
            continue

        if "Sats" not in examined and vitals["Sats"] is None:
            take_action(25)  # Use Sats Probe
            examined.add("Sats")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if events[11]:  # BreathingBibasalCrepitations
            take_action(30)  # Use Non Rebreather Mask
            continue

        # Circulation Assessment
        if "MAP" not in examined and vitals["MAP"] is None:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("MAP")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        # Check and Treat Tachyarrhythmia
        if vitals["HR"] is not None:
            if vitals["HR"] > 150:
                take_action(24)  # Use Monitor Pads (for cardioversion)
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # Give Atropine
                continue

        # Stabilized
        if vitals["Sats"] >= 88 and vitals["RR"] >= 8 and vitals["MAP"] >= 60 and events[3]:
            take_action(48)  # Finish
            break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
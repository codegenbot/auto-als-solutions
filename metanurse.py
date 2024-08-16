import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing if input is invalid
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

        # Cardiac arrest scenario
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compressions
            continue

        # Airway examination
        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(3)  # Examine airway
            examined_vitals.add("airway")
            continue

        # Use Sats probe if no oxygen saturation measurement
        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # Use sats probe
            examined_vitals.add("Sats")
            continue

        # Ensure patient receives oxygen if needed
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if "mask" not in examined_vitals:
                take_action(30)  # Use NonRebreatherMask
                examined_vitals.add("mask")
            else:
                take_action(29)  # Use BagValveMask
            continue

        # Breathing examination
        if any(events[i] > 0 for i in range(7, 15)) and "breathing" not in examined_vitals:
            take_action(4)  # Examine breathing
            examined_vitals.add("breathing")
            continue

        # Use blood pressure cuff if no MAP measurement
        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)  # Use blood pressure cuff
            examined_vitals.add("MAP")
            continue

        # Check blood pressure on monitor
        if vitals["MAP"] is None and "monitor" not in examined_vitals:
            take_action(16)  # View Monitor
            examined_vitals.add("monitor")
            continue

        # Provide fluids if MAP < 60
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        # Disability examination
        if any(events[i] > 0 for i in range(20, 26)) and "disability" not in examined_vitals:
            take_action(6)  # Examine disability
            examined_vitals.add("disability")
            continue

        # Exposure examination
        if any(events[i] > 0 for i in range(26, 33)) and "exposure" not in examined_vitals:
            take_action(7)  # Examine exposure
            examined_vitals.add("exposure")
            continue

        # Rhythm check if MAP low or HR abnormal
        if (vitals["MAP"] is not None and vitals["MAP"] < 60) or (vitals["HR"] and (vitals["HR"] < 60 or vitals["HR"] > 100)):
            take_action(2)  # CheckRhythm
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
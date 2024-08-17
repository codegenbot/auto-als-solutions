import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps = 350
    examined = set()
    actions = []

    def check_measurements(vitals, measurement_times):
        measures = ["HR", "RR", "Glucose", "Temp", "MAP", "Sats", "Resps"]
        for i, measure in enumerate(measures):
            if measure not in examined and measurement_times[i] == 0:
                return actions_dict[measure]
        return None

    actions_dict = {
        "MAP": 27,        # Use Blood Pressure Cuff
        "Sats": 25,       # Use Sats Probe
        "HR": 16,         # View Monitor
    }

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

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        if "Airway" not in examined:
            take_action(3)  # Examine Airway
            examined.add("Airway")
            continue

        meas_action = check_measurements(vitals, measurement_times)
        if meas_action:
            take_action(meas_action)
            vital_str = [k for k, v in actions_dict.items() if v == meas_action][0]
            examined.add(vital_str)
            continue

        if not any(events[3:7]):
            continue

        if "Breathing" not in examined:
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

        if vitals["HR"] is not None:
            if vitals["HR"] > 150:
                take_action(2)  # Check Rhythm
                if any(events[28:32]):  # SVT, AF, Atrial Flutter
                    take_action(24)  # Use Monitor Pads (for cardioversion)
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
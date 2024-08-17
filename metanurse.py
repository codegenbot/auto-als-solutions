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
        "MAP": 27,
        "Sats": 25,
        "HR": 16,
    }

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
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
            take_action(17)
            continue

        if "Airway" not in examined:
            take_action(3)
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
            take_action(4)
            examined.add("Breathing")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["HR"] is not None:
            if vitals["HR"] > 150:
                take_action(2)
                if any(events[28:32]):
                    take_action(24)
                    continue
            elif vitals["HR"] < 50:
                take_action(12)
                continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
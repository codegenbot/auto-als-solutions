import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def get_observations():
        try:
            return list(map(float, input().strip().split()))
        except Exception:
            take_action(48)
            sys.exit()

    steps, examined = 350, set()

    for _ in range(steps):
        observations = get_observations()
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        measured_recent = observations[33:40]
        measurements = observations[46:]

        vitals = {
            "HR": measurements[0] if measured_recent[0] > 0 else None,
            "RR": measurements[1] if measured_recent[1] > 0 else None,
            "Glucose": measurements[2] if measured_recent[2] > 0 else None,
            "Temp": measurements[3] if measured_recent[3] > 0 else None,
            "MAP": measurements[4] if measured_recent[4] > 0 else None,
            "Sats": measurements[5] if measured_recent[5] > 0 else None,
            "Resps": measurements[6] if measured_recent[6] > 0 else None,
        }

        # Cardiac arrest criteria
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        # Airway assessment
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        # Saturation and MAP assessment
        if vitals["Sats"] is None and "Sats" not in examined:
            take_action(25)
            examined.add("Sats")
            continue

        if vitals["MAP"] is None and "MAP" not in examined:
            take_action(27)
            examined.add("MAP")
            continue

        # Breathing assessment
        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        # Improve oxygenation if needed
        if (vitals["Sats"] is not None and vitals["Sats"] < 88):
            take_action(30)
            continue

        # Handle hypotension
        if (vitals["MAP"] is not None and vitals["MAP"] < 60):
            take_action(15)
            continue

        # Check respiratory rate if it's lower than required
        if (vitals["RR"] is not None and vitals["RR"] < 8):
            take_action(29)
            continue

        # Handling unstable tachyarrhythmia if it exists
        if set(events[27:33]) & {i for i in range(27, 33)}:
            take_action(24)
            continue

        # Check for elevated heart rate
        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(17)
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
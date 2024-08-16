import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    vitals_measurements = {"MAP": False, "Sats": False, "HR": False, "RR": False}
    initial_actions_done = False

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if not initial_actions_done:
            take_action(1)
            initial_actions_done = True
            continue

        if not all(examined_vitals):  # Ensure all sections are examined
            if not vitals_measurements["Sats"]:
                take_action(25)  # Use Sats Probe
                vitals_measurements["Sats"] = True
                continue

            take_action(3)  # Examine Airway
            continue

            take_action(4)  # Examine Breathing
            continue

            take_action(5)  # Examine Circulation
            continue

            take_action(6)  # Examine Disability
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["HR"] is not None and (vitals["HR"] < 60 or vitals["HR"] > 150):
            take_action(9)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def measure_vitals():
        if "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
        elif "BP" not in examined:
            take_action(27)
            examined.add("BP")
        else:
            take_action(16)  # View monitor to check all vitals

    actions = 0
    while actions < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            actions += 1
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "Glucose": values[2] if times[2] > 0 else None,
            "Temp": values[3] if times[3] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
            "Resps": values[6] if times[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compression
            break

        if "Airway" not in examined:
            take_action(3)  # Examine Airway
            examined.add("Airway")
            if events[3] > 0:  # AirwayClear
                take_action(0)  # Airway is clear, do nothing
            else:
                take_action(35)  # Perform airway maneuvers if airway issue
            actions += 1
            continue

        measure_vitals()
        actions += 1

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            actions += 1
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            actions += 1
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            actions += 1
            continue

        if vitals["HR"] and (vitals["HR"] < 50 or vitals["HR"] > 150):
            take_action(28)  # Attach Defib Pads
            actions += 1
            continue

    take_action(48)


if __name__ == "__main__":
    stabilize()
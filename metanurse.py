import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start CPR
            continue

        # Airway check
        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(3)  # Examine airway
            examined_vitals.add("airway")
            continue

        if not vitals["Sats"]:
            take_action(25)  # Use sats probe
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use NonRebreatherMask
            continue

        # Breathing check
        if not vitals["RR"]:
            take_action(4)  # Examine breathing
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use BagValveMask
            continue

        # Circulation check
        if not vitals["MAP"]:
            take_action(27)  # Use blood pressure cuff
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if events[15] > 0 and "circulation" not in examined_vitals:
            take_action(5)  # Examine circulation
            examined_vitals.add("circulation")
            continue

        if vitals["HR"] and (vitals["HR"] < 60 or vitals["HR"] > 100):
            take_action(2)  # Check rhythm
            continue

        if events[28] > 0 or events[30] > 0:
            take_action(9)  # Give adenosine for SVT or amiodarone for AF
            continue

        if any(events[i] > 0 for i in range(20, 26)) and "disability" not in examined_vitals:
            take_action(6)  # Examine disability
            examined_vitals.add("disability")
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # Examine exposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
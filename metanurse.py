import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    given_fluids_steps = 0

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

        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(3)  # Examine airway
            examined_vitals.add("airway")
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # Use sats probe
            examined_vitals.add("Sats")
            continue

        if "Sats" in examined_vitals and "ViewMonitor" not in examined_vitals:
            take_action(16)  # View monitor to get actual Sats value
            examined_vitals.add("ViewMonitor")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use NonRebreatherMask
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(4)  # Examine breathing for RR evaluation
            examined_vitals.add("RR")
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use BagValveMask
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)  # Use blood pressure cuff
            examined_vitals.add("MAP")
            continue

        if "MAP" in examined_vitals and "SecondViewMonitor" not in examined_vitals:
            take_action(16)  # View monitor to get MAP value
            examined_vitals.add("SecondViewMonitor")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if given_fluids_steps < 2:
                take_action(15)  # Give fluids
                given_fluids_steps += 1
                continue
            elif given_fluids_steps >= 2:
                take_action(2)  # Check rhythm (for possible cardioversion)
                continue

        if any(events[i] > 0 for i in range(15, 18)) and "circulation" not in examined_vitals:
            take_action(5)  # Examine circulation
            examined_vitals.add("circulation")
            continue

        if vitals["HR"] is not None and (vitals["HR"] < 60 or vitals["HR"] > 100):
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
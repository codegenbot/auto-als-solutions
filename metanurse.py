import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # Fallback on invalid input
            continue

        vitals = {
            "HR": observations[40] if observations[33] > 0 else None,
            "RR": observations[41] if observations[34] > 0 else None,
            "MAP": observations[44] if observations[37] > 0 else None,
            "Sats": observations[45] if observations[38] > 0 else None,
        }

        # Handle cardiac arrest scenarios immediately
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        # Ensure Oxygen Saturation >= 88%
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        # Ensure Respiratory Rate >= 8
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        # Ensure Mean Arterial Pressure >= 60
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        # Initial critical checks: Blood Pressure, Sats Probe, etc.
        if observations[37] == 0:  # Check if MAP was measured
            take_action(27)        # UseBloodPressureCuff
            continue
        if observations[38] == 0:  # Check if Sats was measured
            take_action(25)        # UseSatsProbe
            continue

        # ABCDE sequence examination
        if any(observations[i] > 0 for i in range(3, 7)):
            take_action(3)
            continue
        if any(observations[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue
        if any(observations[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue
        if any(observations[i] > 0 for i in range(20, 26)):
            take_action(6)
            continue
        if any(observations[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        take_action(0)  # Default action if nothing else
    take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    taken_measurements = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing if invalid input length
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if not vitals["Sats"]:
            if 25 not in taken_measurements:
                take_action(25)  # UseSatsProbe
                taken_measurements.add(25)
                continue

        if not vitals["MAP"]:
            if 27 not in taken_measurements:
                take_action(27)  # UseBloodPressureCuff
                taken_measurements.add(27)
                continue
            elif 16 not in taken_measurements:
                take_action(16)  # ViewMonitor
                taken_measurements.add(16)
                continue

        for action in [3, 4, 5, 6, 7, 8]:
            if action not in taken_measurements:
                take_action(action)  # Examine steps
                taken_measurements.add(action)
                break
        
        if len(taken_measurements) == 6:
            take_action(48)  # Finish if all examinations are done
            break

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()

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
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        # Immediate stabilisation actions for critical situations
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        # Ensure Airway (A)
        if any(events[i] > 0 for i in range(3, 7)): 
            take_action(35)  # PerformAirwayManoeuvres
            continue

        # Ensure Breathing (B)
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 25 not in actions_taken:
                actions_taken.add(25)
                take_action(25)  # UseSatsProbe
            else:
                take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Ensure Circulation (C)
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if 27 not in actions_taken:
                actions_taken.add(27)
                take_action(27)  # UseBloodPressureCuff
            else:
                take_action(15)  # GiveFluids
            continue

        # Observations and monitoring
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(2)  # CheckRhythm
            continue

        if 27 not in actions_taken:
            actions_taken.add(27)
            take_action(27)  # UseBloodPressureCuff
            continue
        if 25 not in actions_taken:
            actions_taken.add(25)
            take_action(25)  # UseSatsProbe
            continue
        if 16 not in actions_taken:
            actions_taken.add(16)
            take_action(16)  # ViewMonitor
            continue
        if 38 not in actions_taken:
            actions_taken.add(38)
            take_action(38)  # TakeBloodPressure
            continue

        take_action(0)  # DoNothing

    take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
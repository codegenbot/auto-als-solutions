import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    given_fluids = False
    
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

        # Cardiac Arrest Conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        # Vital Sign Conditions
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if not given_fluids:
                take_action(15)  # GiveFluids
                given_fluids = True
            else:
                take_action(16)  # ViewMonitor
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 25 not in actions_taken:
                take_action(25)  # UseSatsProbe
                actions_taken.add(25)
                continue
            if 30 not in actions_taken:
                take_action(30)  # UseNonRebreatherMask
                actions_taken.add(30)
                continue
            take_action(29)  # UseBagValveMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Generate Needed Observations
        if any(events[i] > 0 for i in range(3, 7)) and 3 not in actions_taken:
            take_action(3)  # ExamineAirway
            actions_taken.add(3)
            continue

        if 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            actions_taken.add(27)
            continue

        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            actions_taken.add(25)
            continue

        if 16 not in actions_taken:
            take_action(16)  # ViewMonitor
            actions_taken.add(16)
            continue

        if 38 not in actions_taken:
            take_action(38)  # TakeBloodPressure
            actions_taken.add(38)
            continue
        
        # Examine Additional Systems if Needed
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            continue
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue
        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)
            continue
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
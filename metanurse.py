import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
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
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start chest compression (assume cardiac arrest)
            continue

        # Airway - A
        if any(events[i] > 0 for i in range(3, 7)) and 3 not in actions_taken:
            take_action(3)
            actions_taken.add(3)
            continue

        # Breathing - B
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 30 not in actions_taken:
                take_action(30)  # UseNonRebreatherMask
                actions_taken.add(30)
                continue
            take_action(29)  # UseBagValveMask
            continue

        if vitals["RR"] is None and 4 not in examined_vitals:
            take_action(4)
            examined_vitals.add(4)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Circulation - C
        if vitals["MAP"] is None and 27 not in examined_vitals:
            take_action(27)  # UseBloodPressureCuff
            examined_vitals.add(27)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if any(events[i] > 0 for i in range(15, 20)) and 5 not in actions_taken:
            take_action(5)
            actions_taken.add(5)
            continue
        
        # Disability - D
        if any(events[i] > 0 for i in range(20, 26)) and 6 not in actions_taken:
            take_action(6)
            actions_taken.add(6)
            continue

        # Exposure - E
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
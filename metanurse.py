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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if any(events[i] > 0 for i in range(28, 37)):
            if 40 not in actions_taken:
                actions_taken.add(40)
                take_action(40)  # DefibrillatorCharge
                continue
            if 40 in actions_taken:
                take_action(39)  # TurnOnDefibrillator
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

        if "MAP" not in vitals or vitals["MAP"] is None:
            if 27 not in actions_taken:
                actions_taken.add(27)
                take_action(27)  # UseBloodPressureCuff
                continue
            if 38 not in actions_taken:
                actions_taken.add(38)
                take_action(38)  # TakeBloodPressure
                continue

        if "Sats" not in vitals or vitals["Sats"] is None:
            if 25 not in actions_taken:
                actions_taken.add(25)
                take_action(25)  # UseSatsProbe
                continue

        if 16 not in actions_taken:
            actions_taken.add(16)
            take_action(16)  # ViewMonitor
            continue
        
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # ExamineAirway
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # ExamineBreathing
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # ExamineCirculation
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # ExamineDisability
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
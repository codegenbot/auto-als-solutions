import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    observed = set()
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start CPR
            continue

        if vitals["MAP"] is None and 27 not in observed:
            take_action(27)  # UseBloodPressureCuff
            observed.add(27)
            continue

        if vitals["Sats"] is None and 25 not in observed:
            take_action(25)  # UseSatsProbe
            observed.add(25)
            continue

        if vitals["RR"] is None and 4 not in observed:
            take_action(4)  # ExamineBreathing
            observed.add(4)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30 if 30 not in observed else 29)  # UseNonRebreatherMask -> UseBagValveMask
            observed.add(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in range(3, 7)) and 3 not in observed:
            take_action(3)  # ExamineAirway
            observed.add(3)
            continue

        if any(events[i] > 0 for i in range(7, 15)) and 4 not in observed:
            take_action(4)  # ExamineBreathing
            observed.add(4)
            continue

        if any(events[i] > 0 for i in range(15, 20)) and 5 not in observed:
            take_action(5)  # ExamineCirculation
            observed.add(5)
            continue

        if any(events[i] > 0 for i in range(20, 26)) and 6 not in observed:
            take_action(6)  # ExamineDisability
            observed.add(6)
            continue

        if any(events[i] > 0 for i in range(26, 33)) and 7 not in observed:
            take_action(7)  # ExamineExposure
            observed.add(7)
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
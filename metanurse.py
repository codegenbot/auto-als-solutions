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

        # Check for cardiac arrest condition
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compressions immediately
            continue

        # Handle low oxygen saturation
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 25 not in actions_taken:
                actions_taken.add(25)
                take_action(25)  # UseSatsProbe
            else:
                take_action(30)  # UseNonRebreatherMask
            continue

        # Handle low respiratory rate
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Handle low MAP
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if 27 not in actions_taken:
                actions_taken.add(27)
                take_action(27)  # UseBloodPressureCuff
            else:
                take_action(15)  # GiveFluids
            continue

        # Ensure initial essential assessments
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

        # Regular Check BP after assessments
        if 38 not in actions_taken:
            actions_taken.add(38)
            take_action(38)  # TakeBloodPressure
            continue

        # Examine Airway
        if any(events[i] > 0 for i in range(3, 7)) and 3 not in actions_taken:
            actions_taken.add(3)
            take_action(3)  # ExamineAirway
            continue

        # Examine Breathing
        if any(events[i] > 0 for i in range(7, 15)) and 4 not in actions_taken:
            actions_taken.add(4)
            take_action(4)  # ExamineBreathing
            continue

        # Examine Circulation
        if any(events[i] > 0 for i in range(15, 20)) and 5 not in actions_taken:
            actions_taken.add(5)
            take_action(5)  # ExamineCirculation
            continue

        # Examine Disability
        if any(events[i] > 0 for i in range(20, 26)) and 6 not in actions_taken:
            actions_taken.add(6)
            take_action(6)  # ExamineDisability
            continue

        # Examine Exposure
        if any(events[i] > 0 for i in range(26, 33)) and 7 not in actions_taken:
            actions_taken.add(7)
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()
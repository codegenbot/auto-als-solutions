import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Cardiac Arrest Conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        # Use monitoring equipment if vitals are unknown
        if vitals["MAP"] is None and 27 not in actions_taken:
            actions_taken.add(27)
            take_action(27)  # UseBloodPressureCuff
            continue

        if vitals["Sats"] is None and 25 not in actions_taken:
            actions_taken.add(25)
            take_action(25)  # UseSatsProbe
            continue

        # Airway Assessment and Management
        if any(events[i] > 0 for i in range(3, 7)):  # Airway events
            take_action(3)  # ExamineAirway
            if events[5] > 0:
                take_action(31)  # UseYankeurSuctionCatheter
            if events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        # Breathing Assessment and Management
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            take_action(4)  # ExamineBreathing
            continue

        # Circulation Assessment and Management
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["HR"] is not None and (
            vitals["HR"] > 100 or events[28] > 0
        ):  # Unstable tachyarrhythmia
            take_action(40)  # DefibrillatorCharge
            actions_taken.add(40)
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation events
            take_action(5)  # ExamineCirculation
            continue

        # Disability Assessment
        if any(events[i] > 0 for i in range(20, 26)):  # Disability events
            take_action(6)  # ExamineDisability
            continue

        # Exposure Assessment
        if any(events[i] > 0 for i in range(26, 33)):  # Exposure events
            take_action(7)  # ExamineExposure
            continue

        # No remaining actions, complete the function
        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    examined = set()

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if "MAP" not in examined and 27 not in actions_taken:
            actions_taken.add(27)
            examined.add("MAP")
            take_action(27)  # UseBloodPressureCuff
            continue

        if "Sats" not in examined and 25 not in actions_taken:
            actions_taken.add(25)
            examined.add("Sats")
            take_action(25)  # UseSatsProbe
            continue

        if any(events[i] > 0 for i in range(3, 7)):  # Airway events
            take_action(3)  # ExamineAirway
            if events[5] > 0:
                take_action(31)  # UseYankeurSuctionCatheter
            if events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        if "Breathing" not in examined:
            examined.add("Breathing")
            take_action(4)  # ExamineBreathing
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            if events[7] > 0:
                take_action(29)  # UseBagValveMask
            if events[14] > 0:
                take_action(30)  # UseNonRebreatherMask
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

        if "Circulation" not in examined:
            examined.add("Circulation")
            take_action(5)  # ExamineCirculation
            continue

        if any(events[i] > 0 for i in range(20, 26)):  # Disability events
            take_action(6)  # ExamineDisability
            continue

        if any(events[i] > 0 for i in range(26, 33)):  # Exposure events
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
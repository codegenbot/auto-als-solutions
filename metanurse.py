import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examine_order = [3, 4, 5, 6, 7, 8]
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if vitals["MAP"] is None and 27 not in actions_taken:
            actions_taken.add(27)
            take_action(27)  # UseBloodPressureCuff
            continue

        if vitals["Sats"] is None and 25 not in actions_taken:
            actions_taken.add(25)
            take_action(25)  # UseSatsProbe
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
 
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(9)  # GiveAdenosine
            continue

        for exam in examine_order:
            if exam not in actions_taken:
                actions_taken.add(exam)
                take_action(exam)
                break
        else:
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()
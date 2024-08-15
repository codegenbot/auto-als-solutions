import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examine_actions = [3, 4, 5, 6, 7]
    measure_actions = [27, 25, 26, 16]

    def evaluate_critical(vitals):
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            return True
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            return True
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            return True
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            return True
        return False

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
            "Glucose": vital_signs_values[2] if vital_signs_times[2] > 0 else None,
            "Temp": vital_signs_values[3] if vital_signs_times[3] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if evaluate_critical(vitals):
            continue

        if all(v in vitals and vitals[v] is not None for v in ["Sats", "RR", "MAP"]):
            take_action(48)  # Finish
            break

        for action in measure_actions:
            take_action(action)
            break

        for action in examine_actions:
            take_action(action)
            break

if __name__ == "__main__":
    stabilize()
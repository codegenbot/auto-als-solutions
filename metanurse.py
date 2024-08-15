import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    initiate_series = [27, 25, 26, 16]
    examine_series = [3, 4, 5, 6, 7]

    def evaluate_critical(vitals):
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            return True
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            return True
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            return True
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            return True
        return False

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
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

        measurements_taken = set()

        for measurement in initiate_series:
            if measurement not in measurements_taken:
                measurements_taken.add(measurement)
                take_action(measurement)
                break
        else:
            for exam in examine_series:
                if exam not in measurements_taken:
                    measurements_taken.add(exam)
                    take_action(exam)
                    break

        if events[5] > 0:
            take_action(31)
            continue
        if events[6] > 0:
            take_action(32)
            continue
        if any(events[3:7]):
            take_action(3)
            continue
        if any(events[7:15]):
            take_action(4)
            continue
        if events[7] > 0:
            take_action(29)
            continue
        if events[14] > 0:
            take_action(19)
            continue
        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(24)
            continue
        if any(events[15:20]):
            take_action(5)
            continue
        if any(events[20:26]):
            take_action(6)
            continue
        if any(events[26:33]):
            take_action(7)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

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

    def get_observations():
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            return None, None, None
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
        return events, vital_signs_times, vitals

    for step in range(350):
        events, vital_signs_times, vitals = get_observations()
        if vitals is None:
            continue
        
        if evaluate_critical(vitals):
            continue

        if events[3] > 0:
            if events[4] > 0 or events[5] > 0 or events[6] > 0:
                take_action(31)
            else:
                take_action(3)
            continue

        if events[7] > 0 or any(events[8:15]):
            take_action(4)
            continue

        if vitals["Sats"] is None:
            take_action(25)
            continue

        if events[15] > 0:
            take_action(5)
            continue

        if vitals["MAP"] is None:
            take_action(27)
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
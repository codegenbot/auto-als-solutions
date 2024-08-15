import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def get_treatment_plan(events, vitals):
        if events[3] > 0:
            return 0
        if events[4] > 0:
            return 31
        if events[5] > 0:
            return 31
        if events[6] > 0:
            return 32
        if vitals["Sats"] is not None:
            if vitals["Sats"] < 65:
                return 17
            elif vitals["Sats"] < 88:
                return 30
        if vitals["RR"] is not None and vitals["RR"] < 8:
            return 29
        if events[7] > 0 or events[8] > 0 or events[9] > 0:
            return 29
        if events[14] > 0:
            return 19
        if vitals["MAP"] is not None:
            if vitals["MAP"] < 20:
                return 17
            elif vitals["MAP"] < 60:
                return 15
        if events[15] > 0 or events[16] > 0:
            return 5
        if events[20] > 0:
            return 0
        if events[19] > 0:
            return 5
        if vitals["HR"] is not None and vitals["HR"] > 150:
            return 24
        if any(events[i] > 0 for i in range(20, 26)):
            return 6
        if vitals["Temp"] is not None and vitals["Temp"] > 0:
            return 0
        if any(events[i] > 0 for i in range(26, 33)):
            return 7
        return 48
    
    measurements_taken = []
    examine_series = [3, 4, 5, 6, 7]
    initiate_series = [27, 25, 26, 16]

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

        action = get_treatment_plan(events, vitals)
        if action != 0:
            take_action(action)
            continue

        for exam in examine_series:
            if exam not in measurements_taken:
                measurements_taken.append(exam)
                take_action(exam)
                break
        else:
            take_action(48)
            break

if __name__ == "__main__":
    stabilize()
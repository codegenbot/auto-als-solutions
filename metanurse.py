import sys

def stabilize():
    max_steps = 350
    essential_measurements = [24, 25, 27, 26]

    def take_action(action):
        print(action)
        sys.stdout.flush()

    def needs_measurements(actions_taken):
        return not all(action in actions_taken for action in essential_measurements)

    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )
        
        HR, RR, Glu, Temp, MAP, Sats, Resps = vital_signs_values
        HR_time, RR_time, Glu_time, Temp_time, MAP_time, Sats_time, Resps_time = vital_signs_times
        
        def get_vital(sign_time, sign_value):
            return sign_value if sign_time > 0 else None

        vitals = {
            "HR": get_vital(HR_time, HR),
            "RR": get_vital(RR_time, RR),
            "MAP": get_vital(MAP_time, MAP),
            "Sats": get_vital(Sats_time, Sats),
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            continue

        if needs_measurements(actions_taken):
            measurement_action = next(action for action in essential_measurements if action not in actions_taken)
            take_action(measurement_action)
            actions_taken.add(measurement_action)
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[5] > 0:
                take_action(31)
            if events[6] > 0:
                take_action(32)
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            if vitals["Sats"] and vitals["Sats"] < 88:
                take_action(30)
            if vitals["RR"] and vitals["RR"] < 8:
                take_action(29)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        if vitals["HR"] and vitals["HR"] > 150:
            take_action(40)
            take_action(41)
            take_action(47)
            take_action(43)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
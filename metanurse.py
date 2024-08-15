import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        sys.stdout.flush()
        actions_taken.add(action)

    required_measurements = [25, 27, 24]
    
    def needs_measurements():
        return not all(action in actions_taken for action in required_measurements)
    
    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action
    
    actions = {
        "unstable_tachycardia": [24, 40, 47],
        "open_airway": 36,
        "suction_airway": 31,
        "non_rebreather": 30,
        "bag_mask": 29,
        "give_fluids": 15,
        "start_compressions": 17,
        "finish": 48
    }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )
        
        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }
        
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(actions["start_compressions"])
            continue
        
        if needs_measurements():
            take_action(next_measurement_action())
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            arrhythmia_events = [31, 32, 33, 34, 35, 36, 37, 38, 39]
            if any(events[i] > 0 for i in arrhythmia_events):
                for action in actions["unstable_tachycardia"]:
                    if action not in actions_taken:
                        take_action(action)
                        break
            else:
                take_action(actions["give_fluids"])
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(actions["non_rebreather"])
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(actions["bag_mask"])
            continue
        
        if events[3] == 0:
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(actions["suction_airway"])
            elif events[6] > 0:
                take_action(actions["open_airway"])
            continue
        
        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)
            if events[7] > 0:
                take_action(actions["bag_mask"])
            if events[13] > 0:
                take_action(5)
            continue
        
        if events[17] == 0:
            take_action(5)
            continue

        if events[20] == 0:
            take_action(6)
            continue

        if events[27] == 0:
            take_action(7)
            continue
        
        take_action(actions["finish"])

if __name__ == "__main__":
    stabilize()
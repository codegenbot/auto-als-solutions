import sys

def stabilize():
    def take_action(action):
        print(action)
    
    required_measurements = [25, 27, 16, 24]
    
    def needs_measurements(actions_taken):
        return any(action not in actions_taken for action in required_measurements)
    
    def next_measurement_action(actions_taken):
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def has_unstable_tachyarrhythmia(events):
        arrhythmia_events = [31, 32, 33, 34, 35, 36, 37, 38]
        return any(events[i] > 0 for i in arrhythmia_events)
    
    actions_taken = set()
    max_steps = 350
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements(actions_taken):
            action = next_measurement_action(actions_taken)
            actions_taken.add(action)
            take_action(action)
            continue
        
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(23)  # Perform Chest Compressions
            continue
        
        if has_unstable_tachyarrhythmia(events) and (vitals["MAP"] is not None and vitals["MAP"] < 60):
            take_action(40)  # Prepare for Cardioversion
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue
        
        if events[4] > 0 or events[5] > 0:
            take_action(31)  # Use Yankeur Suction
            continue

        if events[6] > 0:
            take_action(36)  # Perform Head Tilt Chin Lift
            continue

        if events[7] > 0 or events[10] > 0 or events[11] > 0 or events[12] > 0 or events[13] > 0 or events[14] > 0:
            take_action(29)  # Use Bag Valve Mask
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
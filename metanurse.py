import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    required_measurements = {25, 27, 24}

    def take_action(action):
        print(action)
        sys.stdout.flush()
        actions_taken.add(action)

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (observations[:33], observations[33:40], observations[40:])
        
        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(17)  # Start chest compressions for cardiac arrest
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give IV Fluids
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue
        
        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)  # ExamineAirway
            if events[5] > 0:
                take_action(31)  # Use Yankeur Suction Catheter
            elif events[6] > 0:
                take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        if any(events[i] > 0 for i in range(1, 4)):
            take_action(1)  # CheckSignsOfLife
            take_action(2)  # CheckRhythm
            if any(events[i] > 0 for i in [28, 30, 31, 32, 33, 34, 35, 36]):
                take_action(24)  # Use Monitor Pads
            continue
        
        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
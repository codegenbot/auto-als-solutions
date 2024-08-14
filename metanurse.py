import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        return action == 48

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (observations[:33], observations[33:40], observations[40:])
        
        # Vital signs dictionary
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "CapillaryGlucose": vital_signs_values[2] if vital_signs_times[2] > 0 else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
            "Resps": vital_signs_values[6] if vital_signs_times[6] > 0 else None
        }

        # Perform ABCDE assessment
        if 25 not in actions_taken:
            if take_action(25): break
        if 27 not in actions_taken:
            if take_action(27): break
        if 16 not in actions_taken:
            if take_action(16): break
        if 3 not in actions_taken:
            if take_action(3): break

        if events[6] > 0:
            if take_action(36): break
        if events[4] > 0 or events[5] > 0:
            if take_action(31): break

        if any(events[i] > 0 for i in [29, 30, 31, 32]):
            if 28 not in actions_taken:
                if take_action(28): break
            if take_action(40): break
        
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            if take_action(17): break
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            if take_action(22): break

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if take_action(15): break
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if take_action(30): break
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            if take_action(29): break

        if take_action(48): break

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {25, 27, 16, 3}  # SATs Probe, BP Cuff, Monitor, Airway

    def need_measurements():
        return not required_measurements.issubset(actions_taken)

    def need_measurement_action():
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

        if need_measurements():
            take_action(need_measurement_action())
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(23)  # Resume CPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if any(events[i] > 0 for i in [28, 32, 35, 36]):  # Unstable rhythm indications
                take_action(24)  # Use Monitor Pads for cardioversion
            else:
                take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if any(events[i] > 0 for i in [4, 5]):
            take_action(31)  # Use Yankeur Suction Catheter
            continue

        if any(events[i] > 0 for i in [1, 2, 7, 10, 11, 12, 13, 14]):
            take_action(29)  # Use Bag-Valve Mask
            continue

        # Regularly examining airway, breathing, and circulation:
        if step % 10 == 0:  # Examine every 10 steps
            for action in [3, 4, 5, 2, 6, 7, 8]:  # Examine Airway, Breathing, Circulation, Rhythm, Disability, Exposure, Response
                if action not in actions_taken:
                    take_action(action)
                    actions_taken.add(action)
                    break

        take_action(48)  # Finish if stable

if __name__ == "__main__":
    stabilize()
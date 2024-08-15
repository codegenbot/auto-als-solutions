import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {25, 27, 24}

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Cardiac arrest condition
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compression
            continue

        # Take measurements if needed
        if needs_measurements():
            take_action(next_measurement_action())
            continue

        # Airway assessment and intervention
        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)  # Examine Airway
            if events[5] > 0:
                take_action(31)  # Use Yankeur Suction Catheter
            elif events[6] > 0:
                take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        # Breathing assessment and intervention
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue
        elif vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use bag-valve mask
            continue
        
        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)  # Examine Breathing
            if events[7] > 0:
                take_action(29)  # Use bag-valve mask
            continue

        # Circulation assessment and intervention
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if any(events[i] > 0 for i in range(31, 39)):
                if 24 not in actions_taken:
                    take_action(24)
                elif 40 not in actions_taken:
                    take_action(40)
                elif 47 not in actions_taken:
                    take_action(47)
                else:
                    take_action(48)
            else:
                take_action(15)
            continue

        if any(events[i] > 0 for i in range(1, 4)):
            take_action(8)  # ExamineResponse
            continue

        take_action(48)  # Finish if no appropriate action found

if __name__ == "__main__":
    stabilize()
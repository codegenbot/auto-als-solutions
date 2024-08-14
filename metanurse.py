import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [25, 27, 16, 24]
    assessment_order = [3, 4, 5, 6, 7]

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(48)
            continue

        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if any(action not in actions_taken for action in assessment_order):
            for action in assessment_order:
                if action not in actions_taken:
                    take_action(action)
                    break
            continue

        if any(action not in actions_taken for action in required_measurements):
            for action in required_measurements:
                if action not in actions_taken:
                    take_action(action)
                    break
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(23)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if any(events[i] > 0 for i in range(30, 39)):
                take_action(24)
                continue
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        critical_events_actions = {
            6: 35, 5: 35, 3: 35, 4: 31, 7: 29
        }
        for event, action in critical_events_actions.items():
            if events[event] > 0 and action not in actions_taken:
                take_action(action)
                break
        else:
            take_action(48)

if __name__ == "__main__":
    stabilize()
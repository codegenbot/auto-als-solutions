import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        sys.stdout.flush()
        actions_taken.add(action)

    required_measurements = {24, 25, 27}

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def check_vitals(vitals):
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            return 17
        elif vitals["Sats"] is not None and vitals["Sats"] < 65:
            return 17
        elif vitals["MAP"] is not None and vitals["MAP"] < 60:
            return 15
        elif vitals["Sats"] is not None and vitals["Sats"] < 88:
            return 30
        elif vitals["RR"] is not None and vitals["RR"] < 8:
            return 29
        return None

    def handle_event(events):
        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                return 31
            elif events[6] > 0:
                return 32
        elif any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)
            if events[7] > 0:
                return 29
        elif any(events[i] > 0 for i in range(1, 4)):
            return 8
        return None

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        action = check_vitals(vitals)
        if action:
            take_action(action)
            continue

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        action = handle_event(events)
        if action:
            take_action(action)
            continue

        take_action(0)

if __name__ == "__main__":
    stabilize()
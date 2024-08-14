import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [25, 27, 16, 3]
    measurement_sequence = iter(required_measurements)
    
    def obtain_initial_measurements():
        try:
            next_action = next(measurement_sequence)
            if next_action not in actions_taken:
                take_action(next_action)
                return True
        except StopIteration:
            return False
        return True

    def needs_measurements(vitals):
        return vitals.get("MAP") is None or vitals.get("Sats") is None or vitals.get("RespRate") is None

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if obtain_initial_measurements():
            continue

        if needs_measurements(vitals):
            obtain_initial_measurements()
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(23)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in [4, 5]):
            take_action(31)
            continue

        if events[6] > 0:
            take_action(36)
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(29)
            continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
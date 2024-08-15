import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    required_measurements = {24, 25, 27}

    def take_action(action):
        print(action)
        actions_taken.add(action)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def check_immediate_threats(vitals):
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            return True
        return False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if check_immediate_threats(vitals):
            continue

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if events[3] == 0:
            take_action(3)
            continue
        if any(events[i] > 0 for i in [4, 5, 6]):
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            elif events[6] > 0:
                take_action(32)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue
        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue
        if any(events[i] > 0 for i in [30, 31, 32, 33, 34, 35, 36, 37]):
            take_action(2)
            continue

        if any(events[i] > 0 for i in [21, 22, 23, 24]):
            take_action(6)
            continue

        if any(events[i] > 0 for i in [25, 26, 27]):
            take_action(7)
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] >= 60 and
            vitals["Sats"] is not None and vitals["Sats"] >= 88 and
            vitals["RR"] is not None and vitals["RR"] >= 8):
            take_action(48)
            break

if __name__ == "__main__":
    stabilize()
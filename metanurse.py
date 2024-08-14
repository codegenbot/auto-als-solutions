import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {
        25,  # Use SATs Probe
        27,  # Use Blood Pressure Cuff
        16,  # View Monitor
        3    # Examine Airway
    }

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def has_unstable_tachyarrhythmia(events):
        arrhythmia_events = [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
        return any(events[i] > 0 for i in arrhythmia_events)

    def abcde_prioritize(events):
        if events[3] == 0 and not {4, 5, 6, 7}.isdisjoint(actions_taken):
            return 3
        if any(events[i] > 0 for i in [4, 5]):
            return 31
        if events[6] > 0:
            return 36
        if {8, 9, 10, 11, 12, 13, 14}.isdisjoint(actions_taken):
            return 4
        if any(events[i] > 0 for i in [7, 10, 13, 14]):
            return 29
        if {16, 17, 18}.isdisjoint(actions_taken):
            return 5

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(23)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if has_unstable_tachyarrhythmia(events):
                if 24 not in actions_taken:
                    take_action(24)
                else:
                    take_action(40)
            else:
                take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        next_action = abcde_prioritize(events)
        if next_action:
            take_action(next_action)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
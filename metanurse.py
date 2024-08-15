import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    initial_measurements = [24, 25, 27, 26, 18, 19, 20, 21, 37]

    def next_initial_measurement_action():
        for action in initial_measurements:
            if action not in actions_taken:
                return action

    def needs_initial_measurements():
        return not all(action in actions_taken for action in initial_measurements)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)
            continue

        if needs_initial_measurements():
            take_action(next_initial_measurement_action())
            continue

        # Airway
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            elif events[6] > 0:
                take_action(32)
            continue

        if not any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            continue
        
        # Breathing
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 30 not in actions_taken:
                take_action(30)
                continue
        
        if vitals["RR"] is not None and vitals["RR"] < 8:
            if 29 not in actions_taken:
                take_action(29)
                continue

        if not any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue

        # Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if 15 not in actions_taken:
                take_action(15)
                continue

        tachyarrhythmias = [
            "HeartRhythmSVT", "HeartRhythmVT", "HeartRhythmAF",
            "HeartRhythmAtrialFlutter", "HeartRhythmTorsades", "HeartRhythmVF"
        ]
        if any(events[27 + i] > 0 for i in range(len(tachyarrhythmias))):
            take_action(24)
            take_action(47)
            take_action(43)
            continue

        if not any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue

        # Disability
        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)
            continue

        # Exposure
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
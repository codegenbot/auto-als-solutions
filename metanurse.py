import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    initial_measurements = [24, 25, 27, 26]
    examine_actions = [3, 4, 5, 6, 7]

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
            take_action(17)  # StartChestCompression
            take_action(23)  # ResumeCPR
            continue

        if needs_initial_measurements():
            take_action(next_initial_measurement_action())
            continue

        if any(action in events for action in [7, 9, 10]):
            take_action(35)  # PerformAirwayManoeuvres
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(40)  # Start cardioversion process
            take_action(41)
            take_action(47)
            take_action(43)
            continue

        if step > 5 and any(action not in actions_taken for action in examine_actions):
            for action in examine_actions:
                if action not in actions_taken:
                    take_action(action)
                    break
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
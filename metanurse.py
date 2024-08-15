import sys


def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    initial_measurements = [3, 4, 5, 27, 26, 25]

    def next_initial_measurement_action():
        for action in initial_measurements:
            if action not in actions_taken:
                return action

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
            take_action(23)
            continue

        if any(vitals[k] is None for k in ["MAP", "Sats", "RR"]):
            take_action(next_initial_measurement_action())
            continue

        if not (events[3] > 0):  # No AirwayClear event observed
            take_action(3)
            continue

        if events[5] > 0:  # AirwayVomit
            take_action(31)
            continue
        if events[6] > 0:  # AirwayTongue
            take_action(32)
            continue

        if vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] < 60:
            take_action(15)
            continue

        if events[29] > 0:  # Unstable heart rhythm like SVT
            take_action(9)
            continue

        take_action(48)  # Finish if the patient is stable
        break


if __name__ == "__main__":
    stabilize()
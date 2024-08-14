import sys


def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    def need_measurements():
        return (
            25 not in actions_taken
            or 27 not in actions_taken
            or 16 not in actions_taken
            or 3 not in actions_taken
        )

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
        }

        if need_measurements():
            if 25 not in actions_taken:
                take_action(25)
                continue
            if 27 not in actions_taken:
                take_action(27)
                continue
            if 16 not in actions_taken:
                take_action(16)
                continue
            if 3 not in actions_taken:
                take_action(3)
                continue

        # ABCDE Assessment

        # A - Airway
        take_action(3)
        if events[5] > 0 or events[6] > 0:
            take_action(31)
        if events[7] > 0:
            take_action(29)

        # B - Breathing
        if events[8] == 0:
            take_action(30)
        elif vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)

        # C - Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
        if events[28] > 0:
            take_action(28)
            take_action(40)

        # D - Disability
        take_action(6)

        # E - Exposure
        take_action(7)

        # Check if stabilization conditions are met
        if (
            vitals["MAP"] is not None
            and vitals["MAP"] >= 60
            and vitals["Sats"] is not None
            and vitals["Sats"] >= 88
            and vitals["RespRate"] is not None
            and vitals["RespRate"] >= 8
        ):
            take_action(48)


if __name__ == "__main__":
    stabilize()
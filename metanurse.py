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

    required_measurements = {25, 27, 16, 3}

    def need_measurements():
        return not required_measurements.issubset(actions_taken)

    def need_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        if need_measurements():
            take_action(need_measurement_action())
            continue

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(23)  # Resume CPR
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if events[4] > 0 or events[5] > 0:
            take_action(31)  # Use Yankeur Suction Catheter
            continue

        if events[6] > 0:
            take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        if events[7] > 0 or any(events[i] > 0 for i in [10, 11, 12, 13, 14]):
            take_action(29)  # Use Bag-Valve Mask
            continue

        if any(events[i] > 0 for i in range(28, 33)):
            if 28 not in actions_taken:
                take_action(28)  # Attach Defib Pads
                continue
            take_action(40)  # Defibrillator Charge
            continue

        take_action(48)  # Finish if stable


if __name__ == "__main__":
    stabilize()
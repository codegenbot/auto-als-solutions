import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        sys.stdout.flush()
        if action == 48:
            done = True

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        # Measurements and vitals
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if not all(vitals.values()):
            for action, vital in zip([25, 27, 16, 3], vitals.values()):
                if vital is None:
                    take_action(action)
                    break
            continue

        # Cardiac arrest checks
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            take_action(22)
            continue

        # Airway management
        if events[3] == 0.0:
            take_action(3)
            continue
        if events[4] > 0 or events[5] > 0 or events[6] > 0:
            take_action(31)
            continue

        # Breathing management
        if vitals["Sats"] < 88:
            take_action(30)
            continue
        if vitals["RespRate"] < 8:
            take_action(29)
            continue

        # Circulation management
        if vitals["MAP"] < 60:
            take_action(15)
            continue

        # Disability
        if events[22] > 0 or events[23] > 0:
            take_action(6)
            continue

        # Exposure
        if events[24] > 0 or events[25] > 0 or events[26] > 0 or events[27] > 0:
            take_action(7)
            continue

        # Rhythmic issues
        if events[28] > 0 or events[29] > 0 or events[30] > 0 or events[31] > 0 or events[32] > 0:
            take_action(28)
            continue
        if 28 in actions_taken:
            take_action(24)  # Attach defib pads
            take_action(40)  # Charge defibrillator
            take_action(39)  # Turn on defibrillator
            continue

        if all(x is not None for x in vitals.values()) and (vitals["RespRate"] >= 8 and vitals["Sats"] >= 88 and vitals["MAP"] >= 60):
            take_action(48)
            continue

        # Default to DoNothing
        take_action(0)

if __name__ == "__main__":
    stabilize()
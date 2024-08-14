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
            observations[40:]
        )

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if events[3] == 0:  # Check airway
            take_action(3)
            continue

        if events[2] > 0 or events[4] > 0 or events[5] > 0:  # Clear airway obstructions
            take_action(31)
            continue

        if events[6] > 0:  # Perform head tilt chin lift for airway
            take_action(36)
            continue

        if any([vitals["MAP"], vitals["RespRate"], vitals["Sats"]] is None):  # Check vitals
            if 25 not in actions_taken:
                take_action(25)
                continue
            if 27 not in actions_taken:
                take_action(27)
                continue
            if 16 not in actions_taken:
                take_action(16)
                continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:  # Critical MAP
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:  # Critical Sats
            take_action(22)
            continue

        if unstable_rhythm := any(events[i] > 0 for i in range(29, 34)):  # Unstable rhythms
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:  # Low MAP
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:  # Low Sats
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:  # Low RR
            take_action(29)
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
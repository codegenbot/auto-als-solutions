import sys

def stabilize():
    max_steps = 350
    actions_taken = []
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.append(action)
        print(action)
        if action == 48:
            done = True

    def need_examination():
        return 25 not in actions_taken or 27 not in actions_taken or 16 not in actions_taken or 3 not in actions_taken

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
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                     "MAP", "Sats", "Resps"], vital_signs_values
                )
            )
        }

        # ABCDE Assessment
        # A - Airway
        if 3 not in actions_taken:
            take_action(3)
            continue

        # Clearing airway if vomit or blood is detected
        if events[4] > 0 or events[5] > 0:
            take_action(31)
            continue

        # Clearing obstruction due to tongue
        if events[6] > 0:
            take_action(36)
            continue

        # B - Breathing
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        # C - Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        # Checking for tachyarrhythmia
        unstable_tachyarrhythmia = (
            events[29] > 0 or events[30] > 0 or
            events[31] > 0 or events[32] > 0 or
            events[33] > 0 or events[34] > 0
        )
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue

        # D - Disability, E - Exposure, and Examinations
        if need_examination():
            if 25 not in actions_taken:
                take_action(25)
                continue
            if 27 not in actions_taken:
                take_action(27)
                continue
            if 16 not in actions_taken:
                take_action(16)
                continue

        # Finishing if all checks are stable
        take_action(48)

if __name__ == "__main__":
    stabilize()
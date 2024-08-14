import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        sys.stdout.flush()  # Ensure the action is immediately printed
        if action == 48:
            done = True

    def need_examination():
        return 25 not in actions_taken or 27 not in actions_taken or 16 not in actions_taken or 3 not in actions_taken

    examination_sequence = [25, 27, 16, 3, 4, 5, 6, 7, 8]

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
        
        if need_examination():
            for action in examination_sequence:
                if action not in actions_taken:
                    take_action(action)
                    break
            continue

        if events[4] > 0 or events[5] > 0:
            take_action(31)  # Use Yankeur Suction Catheter
            continue

        if events[6] > 0:
            take_action(36)  # Perform head tilt-chin lift
            continue

        unstable_tachyarrhythmia = any(events[i] > 0 for i in [29, 30, 31, 32])
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)  # Attach defib pads
                continue
            take_action(40)  # Defibrillator charge
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # Start chest compression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # Bag During CPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
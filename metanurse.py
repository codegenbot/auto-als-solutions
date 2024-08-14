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

        if not actions_taken:
            take_action(3)  # Start with airway examination
            continue

        if 25 not in actions_taken:
            take_action(25)  # Place Sats Probe
            continue

        if 27 not in actions_taken:
            take_action(27)  # Use BP Cuff
            continue
            
        if 16 not in actions_taken:
            take_action(16)  # View monitor
            continue

        # Check critical conditions
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # Start Chest Compressions
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # Bag during CPR
            continue

        unstable_tachyarrhythmia = (events[29] > 0 or events[30] > 0 or 
                                    events[31] > 0 or events[32] > 0)
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)  # Attach Defib Pads
                continue
            take_action(40)  # Charge Defib
            continue

        # Stabilize other vitals
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if need_examination():
            if 3 not in actions_taken:
                take_action(3)  # Re-examine Airway if needed
                continue
            take_action(5)  # Default to Examine Breathing

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
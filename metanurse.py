import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:  # Finish
            done = True

    def need_examination():
        return (
            25 not in actions_taken
            or 27 not in_actions_taken
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
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    [
                        "HeartRate",
                        "RespRate",
                        "CapillaryGlucose",
                        "Temperature",
                        "MAP",
                        "Sats",
                        "Resps",
                    ],
                    vital_signs_values,
                )
            )
        }

        # Ensure required examinations are conducted
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
            if 3 not in actions_taken:
                take_action(3)
                continue

        # Airway assessments
        if events[4] > 0 or events[5] > 0:  # Vomit or Blood
            take_action(31)  # Suction
            continue
        if events[6] > 0:  # Tongue Obstruction
            take_action(36)  # Perform Head Tilt-Chin Lift
            continue

        # Breathing - Manage oxygen saturation and respiration rates
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        # Circulation - Handle MAP and tachyarrhythmias
        if vitals["MAP"] is not None and vitals["MAP"] < 20:  # MAP critical
            take_action(17)  # Start Chest Compression (CPR)
            continue
            
        if vitals["MAP"] is not None and vitals["MAP"] < 60:  # MAP low but not critical
            take_action(15)  # Give Fluids
            continue
        
        unstable_tachyarrhythmia = (
            events[29] > 0 or events[30] > 0 or events[31] > 0 or events[32] > 0
        )
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)  # Attach Defib Pads
                continue
            take_action(40)  # Cardioversion (Defibrillator Charge)
            continue

        # CPR if Sats are critically low
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # Bag During CPR
            continue

        # If assessments and stabilizations are satisfactory
        take_action(48)

if __name__ == "__main__":
    stabilize()
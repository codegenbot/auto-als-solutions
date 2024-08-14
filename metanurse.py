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

        # Perform ABCDE assessment
        if 3 not in actions_taken:  # Examine Airway
            take_action(3)
            continue
        if 4 not in actions_taken:  # Examine Breathing
            take_action(4)
            continue
        if 5 not in actions_taken:  # Examine Circulation
            take_action(5)
            continue
        if 6 not in actions_taken:  # Examine Disability
            take_action(6)
            continue
        if 7 not in actions_taken:  # Examine Exposure
            take_action(7)
            continue

        # Attach tools if not done already
        if 25 not in actions_taken:  # Use Sats Probe
            take_action(25)
            continue
        if 27 not in actions_taken:  # Use Blood Pressure Cuff
            take_action(27)
            continue
        if 16 not in actions_taken:  # View Monitor
            take_action(16)
            continue

        # Check vital signs (MAP, RespRate, Sats) and intervene if necessary
        if not vitals["MAP"]:
            take_action(38)
            continue
        if not vitals["RespRate"]:
            take_action(4)
            continue
        if not vitals["Sats"]:
            take_action(16)
            continue

        # Immediate intervention
        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)  # Start Chest Compression
            continue
        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(22)  # Bag During CPR
            continue
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        # Stabilize and finish if all conditions are met
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            take_action(48)
            return

        take_action(48)
        return

if __name__ == "__main__":
    stabilize()
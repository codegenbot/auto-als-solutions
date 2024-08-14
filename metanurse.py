import sys


def stabilize():
    max_steps = 350
    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                [
                    "HeartRate",
                    "RespRate",
                    "CapillaryGlucose",
                    "Temperature",
                    "MAP",
                    "Sats",
                    "Resps",
                ],
            )
        }

        def take_action(action):
            actions_taken.add(action)
            print(action)

        # ABCDE Protocol
        if 3 not in actions_taken:  # A: Airway
            take_action(3)  # Examine Airway
            if events[3]:  # Airway clear
                continue
            elif (
                events[4] or events[5] or events[6]
            ):  # Vomit / Blood / Tongue Obstruction
                take_action(31)  # Use Yankeur Suction Catheter
                continue
            else:
                take_action(35)  # Perform Airway Manoeuvres
                continue

        if 4 not in actions_taken:  # B: Breathing
            take_action(4)  # Examine Breathing
            if vitals["Sats"] is not None and vitals["Sats"] < 65:
                take_action(22)  # Bag During CPR
                continue
            elif Vitals["Sats"] is not None and vitals["Sats"] < 88:
                take_action(30)  # Use Non-Rebreather Mask
                continue
            elif vitals["RespRate"] is not None and vitals["RespRate"] < 8:
                take_action(29)  # Use Bag Valve Mask
                continue

        if 5 not in actions_taken:  # C: Circulation
            take_action(5)  # Examine Circulation
            if vitals["MAP"] is not None and vitals["MAP"] < 20:
                take_action(17)  # Start Chest Compression
                continue
            elif vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(15)  # Give Fluids
                continue
            elif events[29] or events[30] or events[31]:
                take_action(28)  # Attach Defib Pads
                take_action(40)  # Defibrillator Charge
                continue

        if 6 not in actions_taken:  # D: Disability
            take_action(6)  # Examine Disability
            continue

        if 7 not in actions_taken:  # E: Exposure
            take_action(7)  # Examine Exposure
            continue

        # Check for Stabilized Condition
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            take_action(48)
            return

        # Default action if no specific treatment or examination
        take_action(0)  # DoNothing


if __name__ == "__main__":
    stabilize()
import sys


def stabilize():
    max_steps = 350
    steps = 0
    done = False

    def take_action(action):
        nonlocal done
        print(action)
        if action == 48:
            done = True

    checks = {
        "Airway": False,
        "Breathing": False,
        "Circulation": False,
        "Disability": False,
        "Exposure": False,
    }

    while steps < max_steps and not done:
        steps += 1
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        if not checks["Airway"]:
            take_action(3)  # Examine Airway
            checks["Airway"] = True
            continue

        if not checks["Breathing"]:
            take_action(4)  # Examine Breathing
            checks["Breathing"] = True
            continue

        if not checks["Circulation"]:
            take_action(5)  # Examine Circulation
            checks["Circulation"] = True
            continue

        if not checks["Disability"]:
            take_action(6)  # Examine Disability
            checks["Disability"] = True
            continue

        if not checks["Exposure"]:
            take_action(7)  # Examine Exposure
            checks["Exposure"] = True
            continue

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Respond to immediate life-threatening conditions first
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(23)  # Resume CPR
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(29)  # Use Bag Valve Mask
            continue

        # Stabilize conditions according to thresholds
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if any(events[i] > 0 for i in [4, 5]):  # Airway Vomit or Blood
            take_action(31)  # Use Yankeur Suction Catheter
            continue

        if events[6] > 0:  # Airway Tongue
            take_action(36)  # Perform Head Tilt Chin Lift
            continue

        if any(
            events[i] > 0 for i in [7, 10, 11, 12, 13, 14]
        ):  # Breathing None, Snoring, SeeSaw, etc.
            take_action(29)  # Use Bag Valve Mask
            continue

        if any(events[i] > 0 for i in [28, 29, 30, 31, 32]):  # Notable HeartRhythms
            take_action(28)  # Attach Defib Pads
            continue

        take_action(48)  # Finish assessment


if __name__ == "__main__":
    stabilize()
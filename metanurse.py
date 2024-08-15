import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    initial_measurements = [24, 25, 27, 26, 18, 19, 20, 21, 37]

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        actions_taken = set()

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compression
            continue

        if initial_measurements:
            take_action(initial_measurements.pop(0))
            continue

        # Airway
        if not any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # Examine airway
            continue
        if events[5] > 0:  # AirwayVomit
            take_action(31)  # Use Yankeur Suction Catheter
            continue
        if events[6] > 0:  # AirwayTongue
            take_action(32)  # Use Guedel Airway
            continue

        # Breathing
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue
        if not any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # Examine Breathing
            continue

        # Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue
        if not any(events[i] > 0 for i in range(15, 19)):
            take_action(5)  # Examine Circulation
            continue

        # Disability
        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # Examine Disability
            continue

        # Exposure
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # Examine Exposure
            continue

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    step_counter = 0

    while step_counter < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            step_counter += 1
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start CPR
            step_counter += 1
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)  # Use Blood Pressure Cuff
            examined_vitals.add("MAP")
            step_counter += 1
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # Use Sats Probe
            examined_vitals.add("Sats")
            step_counter += 1
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(4)  # Examine Breathing
            examined_vitals.add("RR")
            step_counter += 1
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            step_counter += 1
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30 if "mask" in examined_vitals else 29)  # Use NonRebreatherMask or Bag Valve Mask
            examined_vitals.add("mask")
            step_counter += 1
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            step_counter += 1
            continue

        if not all([vitals["MAP"], vitals["Sats"], vitals["RR"]]):
            take_action(16)  # View Monitor to get Sats & MAP after using Probes (if still missing)
            step_counter += 1
            continue

        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(3)  # Examine Airway
            examined_vitals.add("airway")
            step_counter += 1
            continue

        if any(events[i] > 0 for i in range(7, 15)) and "breathing" not in examined_vitals:
            take_action(4)  # Examine Breathing
            examined_vitals.add("breathing")
            step_counter += 1
            continue

        if any(events[i] > 0 for i in range(15, 20)) and "circulation" not in examined_vitals:
            take_action(5)  # Examine Circulation
            examined_vitals.add("circulation")
            step_counter += 1
            continue

        if any(events[i] > 0 for i in range(20, 26)) and "disability" not in examined_vitals:
            take_action(6)  # Examine Disability
            examined_vitals.add("disability")
            step_counter += 1
            continue

        if any(events[i] > 0 for i in range(26, 33)) and "exposure" not in examined_vitals:
            take_action(7)  # Examine Exposure
            examined_vitals.add("exposure")
            step_counter += 1
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
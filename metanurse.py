import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
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
            continue

        if "monitor" not in examined_vitals:
            take_action(16)  # View monitor
            examined_vitals.add("monitor")
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)  # Use blood pressure cuff
            examined_vitals.add("MAP")
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # Use sats probe
            examined_vitals.add("Sats")
            continue

        if "viewed_after_probe" not in examined_vitals:
            take_action(16)  # View monitor
            examined_vitals.add("viewed_after_probe")
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(4)  # Examine breathing
            examined_vitals.add("RR")
            continue

        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(3)  # Examine airway
            examined_vitals.add("airway")
            continue

        if (
            any(events[i] > 0 for i in range(7, 15))
            and "breathing" not in examined_vitals
        ):
            take_action(4)  # Examine breathing
            examined_vitals.add("breathing")
            continue

        if (
            any(events[i] > 0 for i in range(15, 20))
            and "circulation" not in examined_vitals
        ):
            take_action(5)  # Examine circulation
            examined_vitals.add("circulation")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if (events[29] > 0 or events[30] > 0) and (
            vitals["HR"] is not None and vitals["HR"] > 150
        ):
            take_action(9)  # Give Adenosine or other arrhythmia management
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(
                30 if "mask" not in examined_vitals else 29
            )  # Use NonRebreatherMask or Use BagValveMask
            examined_vitals.add("mask")
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask
            continue

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()
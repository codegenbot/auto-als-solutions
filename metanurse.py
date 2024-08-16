import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    vital_checks = {
        "airway": {"action": 3, "examined": False},
        "breathing": {"action": 4, "examined": False},
        "circulation": {"action": 5, "examined": False},
        "disability": {"action": 6, "examined": False},
        "exposure": {"action": 7, "examined": False},
        "bp_cuff": {"action": 27, "used": False},
        "sats_probe": {"action": 25, "used": False},
        "use_monitor": {"action": 24, "used": False},
    }

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

        if (
            any(events[i] > 0 for i in range(3, 7))
            and not vital_checks["airway"]["examined"]
        ):
            take_action(3)  # Examine airway
            vital_checks["airway"]["examined"] = True
            continue

        if vitals["MAP"] is None and not vital_checks["bp_cuff"]["used"]:
            take_action(27)  # Use blood pressure cuff
            vital_checks["bp_cuff"]["used"] = True
            continue

        if vitals["MAP"] is not None:
            if vitals["MAP"] < 60:
                take_action(15)  # Give fluids
                continue

        if vitals["Sats"] is None and not vital_checks["sats_probe"]["used"]:
            take_action(25)  # Use sats probe
            vital_checks["sats_probe"]["used"] = True
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if "mask" not in vital_checks:
                take_action(30)  # Use NonRebreatherMask
                vital_checks["mask"] = True
            else:
                take_action(29)  # Use BagValveMask
            continue

        if vitals["RR"] is None and not vital_checks["breathing"]["examined"]:
            take_action(4)  # Examine breathing
            vital_checks["breathing"]["examined"] = True
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use BagValveMask
            continue

        if (
            any(events[i] > 0 for i in range(7, 15))
            and not vital_checks["breathing"]["examined"]
        ):
            take_action(4)  # Examine breathing
            vital_checks["breathing"]["examined"] = True
            continue

        if (
            any(events[i] > 0 for i in range(15, 20))
            and not vital_checks["circulation"]["examined"]
        ):
            take_action(5)  # Examine circulation
            vital_checks["circulation"]["examined"] = True
            continue

        if vitals["HR"] is not None and not vital_checks["use_monitor"]["used"]:
            take_action(24)  # Use monitor pads
            vital_checks["use_monitor"]["used"] = True
            continue

        if (
            any(events[i] > 0 for i in range(20, 26))
            and not vital_checks["disability"]["examined"]
        ):
            take_action(6)  # Examine disability
            vital_checks["disability"]["examined"] = True
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # Examine exposure
            continue

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()
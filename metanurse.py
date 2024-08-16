import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

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
            "Glucose": values[2] if times[2] > 0 else None,
            "Temp": values[3] if times[3] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
            "Resps": values[6] if times[6] > 0 else None,
        }

        # Emergency situations: cardiac arrest criteria
        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compressions
            continue

        # Airway assessment
        if events[3] == 0 and "Airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("Airway")
            continue

        # Breathing assessment
        if "Breathing" not in examined:
            take_action(4)  # ExamineBreathing
            examined.add("Breathing")
            continue

        # Circulation assessment
        if "Circulation" not in examined:
            take_action(5)  # ExamineCirculation
            examined.add("Circulation")
            continue

        # Perform necessary actions based on readings (prioritize critical actions)
        if (
            "Monitor" not in examined and times[4] == 0
        ):  # View Monitor if not done and necessary
            take_action(16)
            examined.add("Monitor")
            continue

        if "BP" not in examined and times[4] == 0:  # Apply BP cuff if needed
            take_action(27)
            examined.add("BP")
            continue

        if "SatsProbe" not in examined and times[5] == 0:  # Use Sats Probe if needed
            take_action(25)
            examined.add("SatsProbe")
            continue

        # Treat Hypotension & other critical conditions
        if vitals["MAP"] and vitals["MAP"] < 60:  # Low MAP
            take_action(15)  # Give Fluids
            continue

        if vitals["HR"] and (vitals["HR"] > 150 or vitals["HR"] < 50):
            take_action(24)  # Use Monitor Pads for HR monitoring
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        # If the patient is stable, end scenario
        if all(
            [
                (vitals["Sats"] and vitals["Sats"] >= 88),
                (vitals["RR"] and vitals["RR"] >= 8),
                (vitals["MAP"] and vitals["MAP"] >= 60),
            ]
        ):
            take_action(48)
            break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()
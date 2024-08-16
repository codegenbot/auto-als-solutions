import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    actions_taken = set()

    def examine_vitals():
        if "Monitor" not in examined:
            take_action(16)  # View Monitor
            examined.add("Monitor")
            return True
        if "SatsProbe" not in examined:
            take_action(25)  # Use Sats Probe
            examined.add("SatsProbe")
            return True
        if "BPCuff" not in examined:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("BPCuff")
            return True
        return False

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # Do Nothing
            continue

        events = observations[:33]
        measurements_time = observations[33:40]
        values = observations[40:47]

        vitals = {
            "HR": values[0] if measurements_time[0] > 0 else None,
            "RR": values[1] if measurements_time[1] > 0 else None,
            "Glucose": values[2] if measurements_time[2] > 0 else None,
            "Temp": values[3] if measurements_time[3] > 0 else None,
            "MAP": values[4] if measurements_time[4] > 0 else None,
            "Sats": values[5] if measurements_time[5] > 0 else None,
            "Resps": values[6] if measurements_time[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)  # Start Chest Compression
            continue

        if not events[3]:  # AirwayClear
            if "ExamineAirway" not in actions_taken:
                take_action(3)  # Examine Airway
                actions_taken.add("ExamineAirway")
                continue

        if events[3]:  # AirwayClear
            if "ExamineBreathing" not in actions_taken:
                take_action(4)  # Examine Breathing
                actions_taken.add("ExamineBreathing")
                continue
            if any(events[7:15]):  # Breathing issues
                if events[8]:  # BreathingSnoring
                    take_action(36)  # Perform Head Tilt Chin Lift
                else:
                    take_action(29)  # Use Bag-Valve Mask
                continue

        if examine_vitals():
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)  # Use Monitor Pads (for cardioversion)
                continue
            elif vitals["HR"] > 100:
                take_action(9)  # Give Adenosine
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # Give Atropine
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish


if __name__ == "__main__":
    stabilize()
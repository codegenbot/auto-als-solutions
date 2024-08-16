import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

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
            take_action(0)  # DoNothing
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

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compressions
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("Airway")
            continue

        if events[3]:  # AirwayClear
            if not any(events[7:15]) and "Breathing" not in examined:
                take_action(4)  # ExamineBreathing
                examined.add("Breathing")
                continue

        if events[11]:  # BreathingBibasalCrepitations
            take_action(29)  # UseBagValveMask
            continue
        elif events[12]:  # BreathingWheeze
            take_action(19)  # Open Breathing Drawer
            continue

        if examine_vitals():
            continue

        # Treat based on vitals
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if vitals["HR"] is not None:
            if vitals["HR"] > 150:
                take_action(9)  # Give Adenosine for unstable tachyarrhythmia
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # Give Atropine for bradycardia
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish


if __name__ == "__main__":
    stabilize()
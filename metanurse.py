import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    def examine_vitals():
        if "BPCuff" not in examined:
            take_action(27)  # Use Blood Pressure Cuff
            examined.add("BPCuff")
            return
        if "Monitor" not in examined:
            take_action(16)  # View Monitor
            examined.add("Monitor")
            return
        if "SatsProbe" not in examined:
            take_action(25)  # Use Sats Probe
            examined.add("SatsProbe")
            return

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        values = observations[46:]

        vitals = {
            "HR": values[0] if observations[33] > 0 else None,
            "RR": values[1] if observations[34] > 0 else None,
            "Glucose": values[2] if observations[35] > 0 else None,
            "Temp": values[3] if observations[36] > 0 else None,
            "MAP": values[4] if observations[37] > 0 else None,
            "Sats": values[5] if observations[38] > 0 else None,
            "Resps": values[6] if observations[39] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        if not any(events[3:7]):
            take_action(3)  # ExamineAirway
            continue

        if events[3]:  # AirwayClear
            if not any(events[7:15]):
                take_action(4)  # ExamineBreathing
                continue

        if events[8]:  # BreathingSnoring
            take_action(36)  # PerformHeadTiltChinLift
            continue

        if vitals["Sats"] is None or vitals["MAP"] is None or vitals["RR"] is None:
            examine_vitals()
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] for i in range(28, 33)):
            take_action(24)  # UseMonitorPads
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)  # UseMonitorPads
                continue
            elif vitals["HR"] > 100:
                take_action(9)  # GiveAdenosine
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # GiveAtropine
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
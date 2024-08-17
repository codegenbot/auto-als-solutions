import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined, actions = 350, set(), [16, 25, 27]

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
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

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compressions immediately
            continue

        if not examined:
            if not all([vitals["MAP"], vitals["Sats"]]):
                take_action(16)  # ViewMonitor initially
                continue
            if not vitals["MAP"]:
                take_action(27)  # UseBloodPressureCuff for MAP
                continue
            if not vitals["Sats"]:
                take_action(25)  # UseSatsProbe for Sats
                continue

        if not any(events[3:7]):
            take_action(3)  # ExamineAirway
            examined.add("Airway")
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
        take_action(48)  # Finish if steps exceeded

if __name__ == "__main__":
    stabilize()
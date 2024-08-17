import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()

    for step in range(steps):
        try:
            observations = list(map(float, input().strip().split()))
        except:
            take_action(48)
            return
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        measured_recent = observations[33:40]
        measurements = observations[46:]

        vitals = {
            "HR": measurements[0] if measured_recent[0] > 0 else None,
            "RR": measurements[1] if measured_recent[1] > 0 else None,
            "Glucose": measurements[2] if measured_recent[2] > 0 else None,
            "Temp": measurements[3] if measured_recent[3] > 0 else None,
            "MAP": measurements[4] if measured_recent[4] > 0 else None,
            "Sats": measurements[5] if measured_recent[5] > 0 else None,
            "Resps": measurements[6] if measured_recent[6] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("Airway")
            continue

        if events[3] > 0:
            examined.add("Airway")

        if vitals["Sats"] is None and "Sats" not in examined:
            take_action(25)  # UseSatsProbe
            examined.add("Sats")
            continue

        if vitals["MAP"] is None and "MAP" not in examined:
            take_action(27)  # UseBloodPressureCuff
            examined.add("MAP")
            continue

        if "Breathing" not in examined:
            take_action(4)  # ExamineBreathing
            examined.add("Breathing")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if events[27] > 0 or events[28] > 0 or events[29] > 0 or events[30] > 0 or events[31] > 0 or events[32] > 0:
            take_action(2)  # CheckRhythm
            continue

        if vitals["HR"]:
            if vitals["HR"] > 100:
                take_action(9)  # GiveAdenosine
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
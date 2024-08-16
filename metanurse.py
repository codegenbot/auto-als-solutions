import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def measure_vitals():
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
        elif "BP" not in examined:
            take_action(27)
            examined.add("BP")
        elif "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
        elif "RespRate" not in examined:
            take_action(4)
            examined.add("RespRate")

    actions = 0
    while actions < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            actions += 1
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
            "Resps": values[6] if times[6] > 0 else None
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            break

        if events[3] == 0:  # Check if airway clear
            take_action(3)  # ExamineAirway
            actions += 1
            continue

        measure_vitals()
        actions += 1

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        hr = vitals["HR"]
        if hr and (hr < 50 or hr > 150):
            take_action(28)  # AttachDefibPads
            actions += 1
            continue
        
        break

    take_action(48)  # Finish the assessment

if __name__ == "__main__":
    stabilize()
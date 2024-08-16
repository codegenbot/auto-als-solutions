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
            "HR": values[0] if times[0] != 0 else None,
            "RR": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # Start chest compression
            continue

        if "airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("airway")
            continue

        if any(events[i] > 0 for i in [4, 5, 6]):  # Airway compromised events
            take_action(35)  # PerformAirwayManoeuvres
            continue

        if "SatsProbe" not in examined:
            take_action(25)  # UseSatsProbe
            examined.add("SatsProbe")
            continue

        if "RespRate" not in examined:
            take_action(4)  # ExamineBreathing
            examined.add("RespRate")
            continue

        if "BP" not in examined:
            take_action(27)  # UseBloodPressureCuff
            examined.add("BP")
            continue
        
        if "Monitor" not in examined:
            take_action(16)  # ViewMonitor
            examined.add("Monitor")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue
        
        take_action(48)  # Finish
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
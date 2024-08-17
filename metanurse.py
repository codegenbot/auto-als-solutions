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

        # Parse events and observations
        events = observations[:33]
        measured_recent = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if measured_recent[0] > 0 else None,
            "RR": measurements[1] if measured_recent[1] > 0 else None,
            "Glucose": measurements[2] if measured_recent[2] > 0 else None,
            "Temp": measurements[3] if measured_recent[3] > 0 else None,
            "MAP": measurements[4] if measured_recent[4] > 0 else None,
            "Sats": measurements[5] if measured_recent[5] > 0 else None,
            "Resps": measurements[6] if measured_recent[6] > 0 else None,
        }

        # Immediate stabilization if critical
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        # Check Airway
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("Airway")
            continue

        # Attach and check SATS probe
        if vitals["Sats"] is None and "Sats" not in examined:
            take_action(25)  # UseSatsProbe
            examined.add("Sats")
            continue

        # Attach and check Blood Pressure Cuff
        if vitals["MAP"] is None and "MAP" not in examined:
            take_action(27)  # UseBloodPressureCuff
            examined.add("MAP")
            continue
        
        # Check breathing
        if "Breathing" not in examined:
            take_action(4)  # ExamineBreathing
            examined.add("Breathing")
            continue

        # Treat low oxygen saturation
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        # Treat low MAP
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        
        # Check and treat rhythm issues
        if any(events[27:33]):
            take_action(24)  # UseMonitorPads
            continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()
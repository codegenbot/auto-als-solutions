import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined, current_action_idx = 350, set(), 0
    actions = [16, 25, 27]  # ViewMonitor, UseSatsProbe, UseBloodPressureCuff

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue
        
        events = observations[:33]
        recent_measurements = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if recent_measurements[0] > 0 else None,
            "RR": measurements[1] if recent_measurements[1] > 0 else None,
            "Glucose": measurements[2] if recent_measurements[2] > 0 else None,
            "Temp": measurements[3] if recent_measurements[3] > 0 else None,
            "MAP": measurements[4] if recent_measurements[4] > 0 else None,
            "Sats": measurements[5] if recent_measurements[5] > 0 else None,
            "Resps": measurements[6] if recent_measurements[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if current_action_idx < len(actions):
            take_action(actions[current_action_idx])
            current_action_idx += 1
            continue

        # Airway Exam
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("Airway")
            continue

        # Breathing Exam
        if not events[8] and "Breathing" not in examined:
            take_action(4)  # ExamineBreathing
            examined.add("Breathing")
            continue

        # Breathing Intervention
        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Circulation Exam
        if not events[17:19] and "Circulation" not in examined:
            take_action(5)  # ExamineCirculation
            examined.add("Circulation")
            continue

        # MAP Checks for intervention
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Sats Checks for intervention
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        # HR Checks for intervention
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

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
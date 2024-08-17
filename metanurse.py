import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def get_observations():
        try:
            return list(map(float, input().strip().split()))
        except:
            take_action(48)
            sys.exit()

    steps = 350
    examined = set()
    
    for _ in range(steps):
        observations = get_observations()
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        measured_recent = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if measured_recent[0] > 0 else None,
            "RR": measurements[1] if measured_recent[1] > 0 else None,
            "Temp": measurements[2] if measured_recent[2] > 0 else None,
            "MAP": measurements[3] if measured_recent[3] > 0 else None,
            "Sats": measurements[4] if measured_recent[4] > 0 else None,
            "Resps": measurements[5] if measured_recent[5] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        # Check Airway
        if not any(events[3:7]):
            take_action(3)
            continue

        # Check Breathing
        if vitals["Sats"] is None and "Sats" not in examined:
            take_action(25)
            examined.add("Sats")
            continue

        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        # Check Circulation
        if vitals["MAP"] is None and "MAP" not in examined:
            take_action(27)
            examined.add("MAP")
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        # Check Disability
        if "Disability" not in examined:
            take_action(6)
            examined.add("Disability")
            continue

        # Check Exposure
        if "Exposure" not in examined:
            take_action(7)
            examined.add("Exposure")
            continue

        # Final check and take measure actions
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[27:33]):
            take_action(24)
            continue

        if vitals["HR"] and (vitals["HR"] > 150 or vitals["HR"] < 50):
            take_action(2)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined, current_action_idx = 350, set(), 0
    basic_actions = [16, 25, 27]

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
            take_action(17)
            continue
        
        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue
        
        if "Airway" in examined:
            if any(events[7:15]):
                if events[7]:
                    take_action(29)
                elif events[9]:
                    take_action(36)
                continue
            if not any(events[0:3]) and "Response" not in examined:
                take_action(8)
                examined.add("Response")
                continue
            if not any(events[15:17]) and "Circulation" not in examined:
                take_action(5)
                examined.add("Circulation")
                continue
            if not any(events[21:24]) and "Disability" not in examined:
                take_action(6)
                examined.add("Disability")
                continue
        
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue
        
        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue
        
        if any(events[28:33]) or (vitals["HR"] and vitals["HR"] > 150):
            take_action(24)
            continue
        
        if vitals["HR"]:
            if vitals["HR"] > 100 and vitals["MAP"] < 60:
                take_action(24)
                continue
            elif vitals["HR"] < 50:
                take_action(12)
                continue
        
        if current_action_idx < len(basic_actions):
            take_action(basic_actions[current_action_idx])
            current_action_idx += 1
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
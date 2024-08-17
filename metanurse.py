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

    steps, examined, actions_taken = 350, set(), 0

    for _ in range(steps):
        observations = get_observations()
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

        MAP, Sats, RR, HR = vitals["MAP"], vitals["Sats"], vitals["RR"], vitals["HR"]

        if (Sats and Sats < 65) or (MAP and MAP < 20):
            take_action(17)
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        if Sats is None and "Sats" not in examined:
            take_action(25)
            examined.add("Sats")
            continue

        if MAP is None and "MAP" not in examined:
            take_action(27)
            examined.add("MAP")
            continue

        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        if Sats and Sats < 88:
            take_action(30)
            continue

        if MAP and MAP < 60:
            take_action(15)
            continue

        if RR and RR < 8:
            take_action(29)
            continue

        if HR:
            if HR > 150:
                take_action(9)
                continue
            elif HR < 50:
                take_action(12)
                continue

        actions_taken += 1
        if actions_taken >= steps:
            take_action(48)
            break

    take_action(48)

if __name__ == "__main__":
    stabilize()
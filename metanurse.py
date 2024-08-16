import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = {'airway': False, 'breathing': False, 'circulation': False, 'disability': False, 'exposure': False}

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if not examined_vitals['airway']:
            take_action(3)
            examined_vitals['airway'] = True
            continue

        if vitals["Sats"] is None and not examined_vitals['breathing']:
            take_action(25)
            examined_vitals['breathing'] = True
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is None and not examined_vitals['breathing']:
            take_action(4)
            examined_vitals['breathing'] = True
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is None and not examined_vitals['circulation']:
            take_action(27)
            examined_vitals['circulation'] = True
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if not examined_vitals['circulation']:
            take_action(5)
            examined_vitals['circulation'] = True
            continue

        if vitals["HR"] is not None and (vitals["HR"] < 60 or vitals["HR"] > 100):
            take_action(2)
            continue

        if not examined_vitals['disability']:
            take_action(6)
            examined_vitals['disability'] = True
            continue

        if not examined_vitals['exposure']:
            take_action(7)
            examined_vitals['exposure'] = True
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
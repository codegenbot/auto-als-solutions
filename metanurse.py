import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    steps = {
        'airway': False,
        'breathing': False,
        'circulation': False,
        'disability': False,
        'exposure': False
    }

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = dict()
        vitals["HR"] = values[0] if times[0] > 0 else None
        vitals["RR"] = values[1] if times[1] > 0 else None
        vitals["Glucose"] = values[2] if times[2] > 0 else None
        vitals["Temp"] = values[3] if times[3] > 0 else None
        vitals["MAP"] = values[4] if times[4] > 0 else None
        vitals["Sats"] = values[5] if times[5] > 0 else None
        vitals["Resps"] = values[6] if times[6] > 0 else None

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if not steps['airway']:
            take_action(3)
            steps['airway'] = True
            continue

        if "AirwayClear" in events and steps['airway']:
            if not steps['breathing']:
                take_action(4)
                steps['breathing'] = True
                continue

            if not steps['circulation']:
                take_action(5)
                steps['circulation'] = True
                continue

        if "BreathingEqualChestExpansion" in events and "BreathingBibasalCrepitations" in events:
            if vitals["Sats"] and vitals["Sats"] < 88:
                take_action(30)
                continue

            if vitals["RR"] and vitals["RR"] < 8:
                take_action(29)
                continue

        if "RadialPulseNonPalpable" in events and "HeartSoundsNormal" in events:
            if vitals["HR"]:
                if vitals["HR"] > 150:
                    take_action(24)
                    continue
                elif vitals["HR"] > 100:
                    take_action(24)
                    continue
                elif vitals["HR"] < 50:
                    take_action(12)
                    continue

            if vitals["MAP"] and vitals["MAP"] < 60:
                take_action(15)
                continue

        take_action(16)

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
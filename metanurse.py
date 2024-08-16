import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    vitals_collected = {
        "Monitor": False,
        "SatsProbe": False,
        "BPCuff": False
    }
    
    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:40]
        measurements_present = observations[40:47]
        values = observations[46:]

        vitals = dict(
            HR=values[0] if measurements_present[0] else None,
            RR=values[1] if measurements_present[1] else None,
            Glucose=values[2] if measurements_present[2] else None,
            Temp=values[3] if measurements_present[3] else None,
            MAP=values[4] if measurements_present[4] else None,
            Sats=values[5] if measurements_present[5] else None,
            Resps=values[6] if measurements_present[6] else None,
        )

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        if not any(events[3:7]):  # Check airway events (4 states)
            take_action(3)
            continue

        if "AirwayClear" in events:
            if not any(events[7:15]):  # Check breathing events (8 states)
                take_action(4)
                continue
            if "BreathingSnoring" in events:
                take_action(36)
                continue

        if not vitals_collected["Monitor"]:
            take_action(16)
            vitals_collected["Monitor"] = True
            continue
        if not vitals_collected["SatsProbe"]:
            take_action(25)
            vitals_collected["SatsProbe"] = True
            continue
        if not vitals_collected["BPCuff"]:
            take_action(27)
            vitals_collected["BPCuff"] = True
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

        if any(events[28:32]):  # Detect irregular heart rhythms
            take_action(24)
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(24)
                continue
            elif vitals["HR"] > 100:
                take_action(9)
                continue
            elif vitals["HR"] < 50:
                take_action(12)
                continue

        if all(vitals[k] and vitals[k] >= v for k, v in [("RR", 8), ("Sats", 88), ("MAP", 60)]):
            take_action(48)
            break

        take_action(0)

if __name__ == "__main__":
    stabilize()
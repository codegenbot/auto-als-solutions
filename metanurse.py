import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    drawers_opened = set()

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
            "Glucose": values[2] if times[2] > 0 else None,
            "Temp": values[3] if times[3] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
            "Resps": values[6] if times[6] > 0 else None
        }

        # Cardiac arrest conditions
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)
            continue

        # Airway
        if events[3] == 0 and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        # Breathing
        if "Breathing" not in examined:
            take_action(4)
            examined.add("Breathing")
            continue

        # Circulation
        if "Circulation" not in examined:
            take_action(5)
            examined.add("Circulation")
            continue

        # Measure vitals
        if not vitals["MAP"] or not vitals["Sats"]:
            for check in ["BP", "SatsProbe", "RespRate", "HeartRate"]:
                if check not in examined:
                    action_map = {"BP": 27, "SatsProbe": 25, "RespRate": 4, "HeartRate": 16}
                    take_action(action_map[check])
                    examined.add(check)
                    return

        # Treat hypotension
        if vitals["MAP"] and vitals["MAP"] < 60:
            if "CirculationDrawer" not in drawers_opened:
                take_action(20)
                drawers_opened.add("CirculationDrawer")
                continue
            take_action(15)
            continue

        # Treat low oxygen saturation
        if vitals["Sats"] and vitals["Sats"] < 88:
            if "BreathingDrawer" not in drawers_opened:
                take_action(19)
                drawers_opened.add("BreathingDrawer")
                continue
            take_action(30)
            continue

        # Treat low respiratory rate
        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        # Tachyarrhythmia
        if vitals["HR"] and (vitals["HR"] > 150):
            if "DefibPads" not in drawers_opened:
                take_action(28)
                drawers_opened.add("DefibPads")
                continue
            take_action(2)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()
        return int(action) == 48
    
    for _ in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                     "MAP", "Sats", "Resps"], vital_signs_values
                )
            )
        }

        if vitals["Sats"] is not None and vitals["Sats"] < 65 or \
           vitals["MAP"] is not None and vitals["MAP"] < 20:
            if 28 not in actions_taken:
                if take_action(28): return
            if take_action(40): return
            if take_action(23): return
            continue

        if vitals["MAP"] is None:
            if 27 not in actions_taken:
                if take_action(27): return
            if 16 not in actions_taken:
                if take_action(16): return
            continue

        if vitals["Sats"] is None:
            if 25 not in actions_taken:
                if take_action(25): return
            if 16 not in actions_taken:
                if take_action(16): return
            continue

        if events[4] > 0 or events[5] > 0:
            if take_action(31): return
            continue

        if events[6] > 0:
            if take_action(36): return
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if take_action(15): return
            if take_action(14): return
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if take_action(30): return
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            if take_action(29): return
            continue

        if take_action(48): return

if __name__ == "__main__":
    stabilize()
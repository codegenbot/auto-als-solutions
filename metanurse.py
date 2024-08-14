import sys

def stabilize():
    max_steps = 350
    
    def take_action(action):
        print(action)
        sys.stdout.flush()
    
    actions = []

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_times, vitals = observations[:33], observations[33:40], observations[40:]

        measurements = {
            "RespRate": vitals[1] if vital_times[1] > 0 else None,
            "MAP": vitals[4] if vital_times[4] > 0 else None,
            "Sats": vitals[5] if vital_times[5] > 0 else None,
        }

        if vital_times[5] == 0 and 25 not in actions:
            take_action(25)
            actions.append(25)
            continue
        if vital_times[4] == 0 and 27 not in actions:
            take_action(27)
            actions.append(27)
            continue
        if 16 not in actions:
            take_action(16)
            actions.append(16)
            continue
        if 3 not in actions:
            take_action(3)
            actions.append(3)
            continue

        if measurements["MAP"] is not None and measurements["MAP"] < 20 or measurements["Sats"] is not None and measurements["Sats"] < 65:
            take_action(23)
            continue

        if measurements["MAP"] is not None and measurements["MAP"] < 60:
            take_action(15)
            continue
        if measurements["Sats"] is not None and measurements["Sats"] < 88:
            take_action(30)
            continue
        if measurements["RespRate"] is not None and measurements["RespRate"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in [4, 5]):
            take_action(31)
            continue
        if events[6] > 0:
            take_action(36)
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(29)
            continue

        if measurements["MAP"] >= 60 and measurements["Sats"] >= 88 and measurements["RespRate"] >= 8:
            take_action(48)
            break

if __name__ == "__main__":
    stabilize()
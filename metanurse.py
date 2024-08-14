import sys

def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)
        if action == 48:
            sys.exit()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (observations[:33], observations[33:40], observations[40:])

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if vitals["MAP"] is None or vitals["Sats"] is None or vitals["RespRate"] is None:
            if vital_signs_times[5] == 0:
                take_action(25)
            elif vital_signs_times[4] == 0:
                take_action(27)
            elif vital_signs_times[1] == 0:
                take_action(16)
            else:
                take_action(1)
            continue

        if events[4] > 0 or events[5] > 0 or events[6] > 0:
            take_action(31 if (events[4] > 0 or events[5] > 0) else 36)
            continue

        if events[7] > 0:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(28, 33)):
            if 28 not in set(range(3, 33)):
                take_action(28)
                continue
            take_action(40)
            continue

        if step == max_steps - 1:
            take_action(48)

if __name__ == "__main__":
    stabilize()
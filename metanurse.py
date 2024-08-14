import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    gather_measurements = [25, 27, 16, 24, 3, 4, 5]

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None
        }

        if step < len(gather_measurements) and gather_measurements[step] not in actions_taken:
            take_action(gather_measurements[step])
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(23)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if events[31] > 0 or events[32] > 0 or events[33] > 0 or events[34] > 0 or events[35] > 0 or events[36] > 0 or events[37] > 0 or events[38] > 0:
                take_action(17)
            else:
                take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
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
        if any(events[i] > 0 for i in range(1, 4)):
            take_action(8)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
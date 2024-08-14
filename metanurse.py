import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    actions = {
        "airway": [3, 31, 36, 37],
        "breathing": [4, 29, 30, 22],
        "circulation": [5, 15, 27, 16],
        "disability": [6, 8],
        "exposure": [7]
    }

    def take_action(action):
        print(action)
        actions_taken.add(action)
        if action == 48:
            sys.exit()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                     "MAP", "Sats", "Resps"], vital_signs_values
                )
            )
        }

        if 25 not in actions_taken:
            take_action(25)
            continue
        if 27 not in actions_taken:
            take_action(27)
            continue
        if 16 not in actions_taken:
            take_action(16)
            continue

        if events[4] > 0 or events[5] > 0 or events[6] > 0:
            for action in actions["airway"]:
                if action not in actions_taken:
                    take_action(action)
                    break

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        for section in ["airway", "breathing", "circulation"]:
            for action in actions[section]:
                if action not in actions_taken:
                    take_action(action)
                    break

        if step > 200:
            take_action(48)
            break

        take_action(48)

if __name__ == "__main__":
    stabilize()
import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    examinations_done = set()
    vital_signs_needed = {"MAP", "Sats"}

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

        if vital_signs_needed and not examinations_done:
            if 25 not in actions_taken:
                take_action(25)
                continue
            if 27 not in actions_taken:
                take_action(27)
                continue
            if 16 not in actions_taken:
                take_action(16)
                continue
            if 3 not in actions_taken:
                take_action(3)
                continue
            examinations_done.add(True)

        if events[4] > 0 or events[5] > 0:
            take_action(31)
            continue
        
        if events[6] > 0:
            take_action(36)
            continue

        unstable_tachyarrhythmia = (events[29] > 0 or events[30] > 0 or 
                                    events[31] > 0 or events[32] > 0)
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue

        if vitals["MAP"] is not None:
            if vitals["MAP"] < 20:
                take_action(17)
                continue
            elif vitals["MAP"] < 60:
                take_action(15)
                continue

        if vitals["Sats"] is not None:
            if vitals["Sats"] < 65:
                take_action(22)
                continue
            elif vitals["Sats"] < 88:
                take_action(30)
                continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        take_action(48)

if __name__ == "__main__":
    stabilize()
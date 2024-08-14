import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    def need_examination():
        return 3 not in actions_taken or 4 not in actions_taken or 5 not in actions_taken or 6 not in actions_taken or 7 not in actions_taken

    for step in range(max_steps):
        if done:
            break

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

        if need_examination():
            if 3 not in actions_taken:
                take_action(3)
                continue
            if 4 not in actions_taken:
                take_action(4)
                continue
            if 5 not in actions_taken:
                take_action(5)
                continue
            if 6 not in actions_taken:
                take_action(6)
                continue
            if 7 not in actions_taken:
                take_action(7)
                continue

        if events[4] > 0 or events[5] > 0:
            if 31 not in actions_taken:
                take_action(31)
                continue
        if events[6] > 0:
            if 36 not in actions_taken:
                take_action(36)
                continue

        unstable_tachyarrhythmia = (events[29] > 0 or events[30] > 0 or events[31] > 0 or events[32] > 0)
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)
                continue
            if 40 not in actions_taken:
                take_action(40)
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

        if (vitals["MAP"] is not None and vitals["MAP"] >= 60 and
            vitals["Sats"] is not None and vitals["Sats"] >= 88 and
            vitals["RespRate"] is not None and vitals["RespRate"] >= 8):
            take_action(48)
            return
        
        take_action(0)

if __name__ == "__main__":
    stabilize()
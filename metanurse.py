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

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_sign_timestamps, vital_sign_values = observations[:33], observations[33:40], observations[40:]

        measured_vitals = {
            "HeartRate": vital_sign_values[0] if vital_sign_timestamps[0] > 0 else None,
            "RespRate": vital_sign_values[1] if vital_sign_timestamps[1] > 0 else None,
            "MAP": vital_sign_values[4] if vital_sign_timestamps[4] > 0 else None,
            "Sats": vital_sign_values[5] if vital_sign_timestamps[5] > 0 else None,
        }

        if events[6] or events[4] or events[5]:
            take_action(3 if "ExamineAirway" not in actions_taken else 35)
            continue

        if measured_vitals["Sats"] is None:
            take_action(25)
            continue
        if measured_vitals["MAP"] is None:
            take_action(27)
            continue
        if "ExamineCirculation" not in actions_taken:
            take_action(5)
            continue
        if "ExamineBreathing" not in actions_taken:
            take_action(4)
            continue

        if any(events[i] for i in range(28, 33)):
            if 28 not in actions_taken:
                take_action(28)
            else:
                take_action(40)
            continue

        if measured_vitals["MAP"] is not None and measured_vitals["MAP"] < 20:
            take_action(17)
            continue
        
        if measured_vitals["Sats"] is not None and measured_vitals["Sats"] < 65:
            take_action(22)
            continue

        if measured_vitals["MAP"] is not None and measured_vitals["MAP"] < 60:
            take_action(15)
            continue

        if measured_vitals["Sats"] is not None and measured_vitals["Sats"] < 88:
            take_action(30)
            continue

        if measured_vitals["RespRate"] is not None and measured_vitals["RespRate"] < 8:
            take_action(29)
            continue

        if all(v is not None for v in measured_vitals.values()) and measured_vitals["Sats"] >= 88 and measured_vitals["RespRate"] >= 8 and measured_vitals["MAP"] >= 60:
            take_action(48)

if __name__ == "__main__":
    stabilize()
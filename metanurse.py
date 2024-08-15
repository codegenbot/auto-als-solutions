import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    examined = {"airway": False, "breathing": False, "circulation": False, "disability": False, "exposure": False}
    
    def take_action(action):
        print(action)
        sys.stdout.flush()
        actions_taken.add(action)

    def need_examination():
        if not examined["airway"]:
            return 3, "airway"
        if not examined["breathing"]:
            return 4, "breathing"
        if not examined["circulation"]:
            return 5, "circulation"
        if not examined["disability"]:
            return 6, "disability"
        if not examined["exposure"]:
            return 7, "exposure"
        return None, None
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            continue

        next_action, to_examine = need_examination()
        if next_action:
            take_action(next_action)
            examined[to_examine] = True
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if any(events[i] > 0 for i in range(27, 33)):
            take_action(43)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
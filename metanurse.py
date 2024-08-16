import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def obtain_vitals(vitals, times):
        for idx, key in enumerate(vitals.keys()):
            if times[idx] == 0:
                vitals[key] = None
            else:
                vitals[key] = vitals[key]
        return vitals

    actions_taken = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0],
            "RR": values[1],
            "MAP": values[4],
            "Sats": values[5],
        }

        vitals = obtain_vitals(vitals, times)

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if "MAP" in vitals and vitals["MAP"] is None:
            take_action(27)
            continue
        if "Sats" in vitals and vitals["Sats"] is None:
            take_action(25)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if 15 not in actions_taken:
                take_action(15)
                actions_taken.add(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if 30 not in actions_taken:
                take_action(30)
                actions_taken.add(30)
                continue
            take_action(29)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[3:7]):
            take_action(3)
            continue

        if any(events[7:15]):
            take_action(4)
            continue

        if any(events[15:20]):
            take_action(5)
            continue

        if any(events[20:26]):
            take_action(6)
            continue

        if any(events[26:33]):
            take_action(7)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
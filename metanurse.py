import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    initial_measurements = [24, 25, 27, 26]
    examined_parts = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if not examined_parts.issuperset(initial_measurements):
            for action in initial_measurements:
                if action not in examined_parts:
                    examined_parts.add(action)
                    take_action(action)
                    break
            continue

        if not examined_parts.issuperset({3, 4, 5, 6, 7}):
            if 3 not in examined_parts:
                examined_parts.add(3)
                take_action(3)
                continue
            if 4 not in examined_parts:
                examined_parts.add(4)
                take_action(4)
                continue
            if 5 not in examined_parts:
                examined_parts.add(5)
                take_action(5)
                continue
            if 6 not in examined_parts:
                examined_parts.add(6)
                take_action(6)
                continue
            if 7 not in examined_parts:
                examined_parts.add(7)
                take_action(7)
                continue

        if any(events[i] > 0 for i in range(3, 7)):
            if events[5] > 0:
                take_action(31)
            if events[6] > 0:
                take_action(32)
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
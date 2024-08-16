import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    for _ in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        HR, RR, MAP, Sats = (
            values[0] if times[0] > 0 else None,
            values[1] if times[1] > 0 else None,
            values[4] if times[4] > 0 else None,
            values[5] if times[5] > 0 else None,
        )

        if (Sats is not None and Sats < 65) or (MAP is not None and MAP < 20):
            take_action(17)
            continue

        if MAP is None:
            take_action(27)
            continue
        if Sats is None:
            take_action(25)
            continue
        if RR is None:
            take_action(4)
            continue

        if MAP < 60:
            take_action(15)
            continue

        if Sats < 88:
            take_action(30)
            continue

        if RR < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            continue

        take_action(48)
        break


if __name__ == "__main__":
    stabilize()
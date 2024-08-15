import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        def check_critical():
            if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
                vitals["MAP"] is not None and vitals["MAP"] < 20):
                take_action(17)
                return True
            return False

        if check_critical():
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

        if any(events[i] > 0 for i in range(27, 33)):  # Check heart rhythm
            take_action(24)  # Use monitor pads
            take_action(16)  # View monitor
            take_action(28)  # Attach defib pads
            take_action(43)  # Defibrillator pace
            continue

        if times[4] == 0:
            take_action(27)
            continue
        if times[5] == 0:
            take_action(25)
            continue
        if times[6] == 0:
            take_action(16)
            continue
        if times[4] == 0:
            take_action(38)
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
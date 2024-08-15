import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    initial_actions = [25, 27, 16]  # UseSatsProbe, UseBloodPressureCuff, ViewMonitor
    initial_actions_taken = 0

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        if not any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            continue
        if not any(events[i] > 0 for i in range(7, 15)) and initial_actions_taken >= 3:
            take_action(4)
            continue
        if not any(events[i] > 0 for i in range(15, 20)) and initial_actions_taken >= 3:
            take_action(5)
            continue
        if not any(events[i] > 0 for i in range(20, 26)) and initial_actions_taken >= 3:
            take_action(6)
            continue
        if not any(events[i] > 0 for i in range(26, 33)) and initial_actions_taken >= 3:
            take_action(7)
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

        if vitals["HR"] is not None and (vitals["HR"] > 150 or vitals["HR"] < 60):
            take_action(24)
            continue

        if initial_actions_taken < 3:
            take_action(initial_actions[initial_actions_taken])
            initial_actions_taken += 1
            continue

        take_action(48)
        break


if __name__ == "__main__":
    stabilize()
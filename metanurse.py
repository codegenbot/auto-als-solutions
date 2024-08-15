import sys

def stabilize():
    max_steps = 350
    steps_taken = 0
    actions_taken = set()

    def take_action(action):
        nonlocal steps_taken
        print(action)
        steps_taken += 1
        actions_taken.add(action)

    initial_actions = [24, 25, 27, 26, 18, 19, 20, 21]

    while steps_taken < max_steps:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events, vitals_time, vitals_values = observations[:33], observations[33:40], observations[40:]
        vitals = {
            "HR": vitals_values[0] if vitals_time[0] > 0 else None,
            "RR": vitals_values[1] if vitals_time[1] > 0 else None,
            "MAP": vitals_values[4] if vitals_time[4] > 0 else None,
            "Sats": vitals_values[5] if vitals_time[5] > 0 else None,
        }

        if any(vitals[m] is None for m in ["RR", "MAP", "Sats"]) and steps_taken < len(initial_actions):
            if initial_actions[steps_taken] not in actions_taken:
                take_action(initial_actions[steps_taken])
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            take_action(23)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[5] > 0:
                take_action(31)
            if events[6] > 0:
                take_action(32)
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
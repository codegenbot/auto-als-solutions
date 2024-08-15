import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    attached_devices = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        attached_devices.add(action)

    required_measurements = [24, 25, 27]

    def attach_devices():
        for action in required_measurements:
            if action not in attached_devices:
                return action
        return None

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        device_action = attach_devices()
        if device_action:
            take_action(device_action)
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            elif events[6] > 0:
                take_action(32)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        tachyarrhythmias = [27, 28, 29, 30, 34, 38]
        if any(events[i] > 0 for i in tachyarrhythmias):
            take_action(24)
            take_action(43)
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()
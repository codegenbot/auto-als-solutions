import sys


def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_actions = [
        24,
        25,
        27,
    ]  # UseMonitorPads, UseSatsProbe, UseBloodPressureCuff
    required_steps = {
        33: 1,
        34: 2,
    }  # ExamineRhythm for 33 (HeartRhythm), CheckSignsOfLife for 34

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
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

        # Immediate actions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # StartChestCompression
            continue

        # Required measurement actions
        if any(action not in actions_taken for action in required_actions):
            for action in required_actions:
                if action not in actions_taken:
                    take_action(action)
                    break

        # Actions based on events
        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)  # ExamineAirway
            take_action(31 if events[4] > 0 or events[5] > 0 else 32)
            continue

        # Stabilize if vital signs are critical
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if any(events[i] > 0 for i in range(1, 4)):
            take_action(8)  # ExamineResponse
            continue

        if any(events[i] > 0 for i in required_steps):
            for i in required_steps:
                if events[i] > 0:
                    take_action(required_steps[i])
                    break

        take_action(48)


if __name__ == "__main__":
    stabilize()
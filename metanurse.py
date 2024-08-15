import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        sys.stdout.flush()  # Ensure output is immediately flushed.
        actions_taken.add(action)

    required_measurement_actions = [24, 25, 27]

    def next_measurement_action():
        for action in required_measurement_actions:
            if action not in actions_taken:
                return action
        return None

    def needs_measurements():
        return not all(action in actions_taken for action in required_measurement_actions)

    def get_vital_signs(vital_signs_times, vital_signs_values):
        return {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events, vital_signs_times, vital_signs_values = (observations[:33], observations[33:40], observations[40:])
        vitals = get_vital_signs(vital_signs_times, vital_signs_values)

        # Check for cardiac arrest
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # StartChestCompression
            continue

        # Attach necessary monitors if not already done
        if needs_measurements():
            next_action = next_measurement_action()
            if next_action:
                take_action(next_action)
            continue

        # Examine Airway if any airway event is relevant
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # ExamineAirway
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # UseYankeurSucionCatheter
            elif events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        # Apply oxygen if saturation level is low
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        # Assist breathing if respiratory rate is low
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Examine Breathing if relevant events are detected
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # ExamineBreathing
            continue

        # Infuse fluids if mean arterial pressure is low
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Examine Circulation if relevant events are detected
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # ExamineCirculation
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
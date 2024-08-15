import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {24, 25, 27}

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action
        return None

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
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

        # Cardiac Arrest Check
        if (vitals["MAP"] and vitals["MAP"] < 20) or (vitals["Sats"] and vitals["Sats"] < 65):
            take_action(17)  # StartChestCompression
            continue

        # Measurement Action
        measurement_action = next_measurement_action()
        if measurement_action:
            take_action(measurement_action)
            continue

        # Check Airway Regularly
        if any(events[i] > 0 for i in [3, 4, 5, 6]):  # Airway events
            take_action(3)  # ExamineAirway
            if events[4] > 0:
                take_action(31)  # UseYankeurSucionCatheter
            if events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        # Breathing Check
        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            take_action(4)  # ExamineBreathing
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Circulation Check
        if any(events[i] > 0 for i in range(15, 20)):  # Circulation events
            take_action(5)  # ExamineCirculation
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Disability Check
        if any(events[i] > 0 for i in range(20, 25)):  # Disability events
            take_action(6)  # ExamineDisability
            continue

        # Exposure Check
        if any(events[i] > 0 for i in range(25, 33)):  # Exposure events
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
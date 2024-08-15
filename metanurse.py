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
    
    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def prioritize_action_for_airway(events):
        if events[4] > 0:
            return 31  # UseYankeurSucionCatheter
        if events[6] > 0:
            return 32  # UseGuedelAirway
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

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            continue

        measurement_action = next_measurement_action()
        if measurement_action:
            take_action(measurement_action)
            continue

        airway_action = prioritize_action_for_airway(events)
        if airway_action:
            take_action(3)  # ExamineAirway
            take_action(airway_action)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            take_action(4)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation events
            take_action(5)
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()
import sys


def parse_input():
    return list(map(float, sys.stdin.readline().strip().split()))


def main():
    steps = 0
    while steps < 350:
        observations = parse_input()
        event_relevances = observations[:33]
        vital_signs_relevances = observations[33:40]
        vital_signs_measurements = observations[40:]

        # Check for immediate life-threatening conditions
        if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
            print(17)  # Start chest compression due to cardiac arrest
            continue

        # Airway assessment and treatment
        if not any(event_relevances[i] > 0 for i in [3, 4, 5]):
            print(36)  # Perform head-tilt chin-lift
            continue

        # Breathing assessment and treatment
        if vital_signs_relevances[5] > 0 and vital_signs_measurements[5] < 88:
            print(30)  # Use non-rebreather mask
            continue
        if vital_signs_relevances[6] > 0 and vital_signs_measurements[6] < 8:
            print(29)  # Use bag valve mask
            continue

        # Circulation assessment and treatment
        if vital_signs_relevances[4] > 0 and vital_signs_measurements[4] < 60:
            print(20)  # Open circulation drawer
            continue

        # Check response if no immediate actions are needed
        if not any(event_relevances[i] > 0 for i in range(3)):
            print(8)  # Check response
            continue

        # Examine exposure if no other actions are needed
        if not any(event_relevances[i] > 0 for i in range(26, 33)):
            print(7)  # Examine exposure
            continue

        # Finish if stabilized
        if all(vital_signs_measurements[i] >= [60, 88, 8][i] for i in range(3)):
            print(48)  # Finish
            return

        # Default action if unsure
        print(0)  # Do nothing

        steps += 1


if __name__ == "__main__":
    main()
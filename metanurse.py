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

        # Check for cardiac arrest conditions
        if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
            print(48)  # Finish due to cardiac arrest
            return

        # Ensure recent vital signs measurements
        if not all(vital_signs_relevances):
            print(16)  # ViewMonitor to get recent measurements
            continue

        # Check and address airway issues
        if not any(event_relevances[i] > 0 for i in [3, 4, 5]):
            print(36)  # Perform head-tilt chin-lift
            continue

        # Check and address breathing issues
        if vital_signs_measurements[6] < 8:
            print(29)  # Use bag valve mask
            continue
        elif vital_signs_measurements[5] < 88:
            print(30)  # Use non-rebreather mask
            continue

        # Check and address circulation issues
        if vital_signs_measurements[4] < 60:
            print(20)  # Open circulation drawer
            continue

        # Finish if stabilized according to the criteria
        if all(vital_signs_measurements[i] >= [60, 88, 8][i] for i in range(3)):
            print(48)  # Finish if stabilized
            return

        steps += 1


if __name__ == "__main__":
    main()
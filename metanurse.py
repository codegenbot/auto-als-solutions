import sys


def parse_input():
    return list(map(float, sys.stdin.readline().strip().split()))


def main():
    steps = 0
    airway_clear = False
    breathing_sufficient = False
    circulation_sufficient = False

    while steps < 350:
        observations = parse_input()
        event_relevances = observations[:33]
        vital_signs_relevances = observations[33:40]
        vital_signs_measurements = observations[40:]

        # Check for cardiac arrest conditions
        if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
            print(48)  # Finish due to cardiac arrest
            return

        # Airway Assessment
        if not airway_clear:
            if any(event_relevances[i] > 0 for i in [3, 4, 5]):
                airway_clear = True
            else:
                print(36)  # Perform head-tilt chin-lift
                continue

        # Breathing Assessment
        if not breathing_sufficient:
            if vital_signs_relevances[6] > 0 and vital_signs_measurements[6] >= 8:
                breathing_sufficient = True
            elif vital_signs_relevances[5] > 0 and vital_signs_measurements[5] < 88:
                print(30)  # Use non-rebreather mask
                continue
            else:
                print(29)  # Use bag valve mask
                continue

        # Circulation Assessment
        if not circulation_sufficient:
            if vital_signs_relevances[4] > 0 and vital_signs_measurements[4] >= 60:
                circulation_sufficient = True
            else:
                print(20)  # Open circulation drawer
                continue

        # Check if stabilized
        if airway_clear and breathing_sufficient and circulation_sufficient:
            print(48)  # Finish if stabilized
            return

        steps += 1


if __name__ == "__main__":
    main()
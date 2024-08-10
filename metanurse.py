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
            print(48)  # Finish due to cardiac arrest
            return

        # Address Airway issues
        if not any(event_relevances[i] > 0 for i in [3, 4, 5]):
            print(36)  # Perform Head-tilt chin-lift
            continue

        # Check and stabilize Breathing
        if vital_signs_relevances[5] > 0 and vital_signs_measurements[5] < 88:
            print(30)  # Use non-rebreather mask
            continue
        if vital_signs_relevances[6] > 0 and vital_signs_measurements[6] < 8:
            print(29)  # Use bag valve mask
            continue

        # Check and stabilize Circulation
        if vital_signs_relevances[4] > 0 and vital_signs_measurements[4] < 60:
            print(20)  # Open circulation drawer
            continue

        # Check Disability (Level of Consciousness)
        if not any(event_relevances[i] > 0 for i in range(3)):
            print(8)  # Check response
            continue

        # Check Exposure (Skin, Temperature)
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
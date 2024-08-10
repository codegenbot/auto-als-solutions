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

        # Check for critical conditions
        if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
            print(48)  # Finish
            return

        # Initial Assessments
        if not any(event_relevances[i] > 0 for i in [3, 4, 5]):  # Airway clear
            print(36)  # PerformHeadTiltChinLift or 37 PerformJawThrust
        elif (
            vital_signs_relevances[6] > 0 and vital_signs_measurements[6] < 8
        ):  # Breathing insufficient
            print(29)  # UseBagValveMask
        elif (
            vital_signs_relevances[4] > 0 and vital_signs_measurements[4] < 60
        ):  # Circulation insufficient
            print(20)  # OpenCirculationDrawer
        elif (
            vital_signs_relevances[5] > 0 and vital_signs_measurements[5] < 88
        ):  # Low sats
            print(30)  # UseNonRebreatherMask
        else:
            # Check for stabilization and take appropriate actions
            if all(vital_signs_measurements[i] >= [60, 88, 8][i] for i in range(3)):
                print(48)  # Finish if stabilized
            else:
                print(0)  # DoNothing as a fallback

        steps += 1


if __name__ == "__main__":
    main()
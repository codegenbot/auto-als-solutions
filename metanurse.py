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

        # ABCDE Assessment and Stabilization
        if any(event_relevances[i] > 0 for i in [3, 4, 5]):  # Airway issues
            print(3)  # ExamineAirway
        elif (
            vital_signs_measurements[6] < 8 or vital_signs_measurements[5] < 88
        ):  # Breathing issues
            print(4)  # ExamineBreathing
            if vital_signs_measurements[6] < 8:
                print(29)  # UseBagValveMask
            if vital_signs_measurements[5] < 88:
                print(30)  # UseNonRebreatherMask
        elif vital_signs_measurements[4] < 60:  # Circulation issues
            print(5)  # ExamineCirculation
            print(20)  # OpenCirculationDrawer
            print(15)  # GiveFluids
        elif any(event_relevances[i] > 0 for i in range(3)):  # Response issues
            print(8)  # ExamineResponse
        else:
            # Check for stabilization and take appropriate actions
            if all(vital_signs_measurements[i] >= [60, 88, 8][i] for i in range(3)):
                print(48)  # Finish if stabilized
            else:
                # Prioritize actions based on current status
                if vital_signs_measurements[4] < 60:
                    print(20)  # OpenCirculationDrawer
                elif vital_signs_measurements[5] < 88:
                    print(30)  # UseNonRebreatherMask
                elif vital_signs_measurements[6] < 8:
                    print(29)  # UseBagValveMask
                else:
                    print(0)  # DoNothing

        steps += 1


if __name__ == "__main__":
    main()
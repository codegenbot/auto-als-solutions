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
        if not any(event_relevances[i] > 0 for i in [3, 4, 5]):  # No Airway issues
            if not any(event_relevances[i] > 0 for i in [6, 7, 8]) and (
                vital_signs_relevances[6] > 0 and vital_signs_measurements[6] >= 8
            ):  # No Breathing issues
                if (
                    vital_signs_relevances[4] > 0 and vital_signs_measurements[4] >= 60
                ) and (
                    vital_signs_relevances[5] > 0 and vital_signs_measurements[5] >= 88
                ):  # No Circulation issues
                    if not any(
                        event_relevances[i] > 0 for i in range(3)
                    ):  # No Response issues
                        if not any(
                            event_relevances[i] > 0 for i in range(26, 33)
                        ):  # No Exposure issues
                            print(48)  # Finish if stabilized
                        else:
                            print(7)  # ExamineExposure
                    else:
                        print(8)  # ExamineResponse
                else:
                    if (
                        vital_signs_relevances[4] > 0
                        and vital_signs_measurements[4] < 60
                    ):
                        print(20)  # OpenCirculationDrawer
                    elif (
                        vital_signs_relevances[5] > 0
                        and vital_signs_measurements[5] < 88
                    ):
                        print(30)  # UseNonRebreatherMask
            else:
                print(4)  # ExamineBreathing
        else:
            print(3)  # ExamineAirway

        steps += 1


if __name__ == "__main__":
    main()
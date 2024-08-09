import sys
import math


def parse_input():
    return list(map(float, sys.stdin.readline().strip().split()))


def main():
    steps = 0
    stabilized = False
    while steps < 350 and not stabilized:
        observations = parse_input()
        event_relevances = observations[:33]
        vital_signs_relevances = observations[33:40]
        vital_signs_measurements = observations[40:]

        # Check for critical conditions
        if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
            print(48)  # Finish
            return

        # Check if John is stabilized
        if (
            event_relevances[3] > 0
            and vital_signs_measurements[5] >= 88  # AirwayClear
            and vital_signs_measurements[6] >= 8  # Sats >= 88%
            and vital_signs_measurements[4] >= 60  # Respiratory rate >= 8
        ):  # MAP >= 60mmHg
            stabilized = True
            print(48)  # Finish
            continue

        # ABCDE Assessment and Stabilization
        if vital_signs_relevances[4] == 0 or vital_signs_measurements[4] < 60:
            print(5)  # ExamineCirculation
        elif vital_signs_relevances[5] == 0 or vital_signs_measurements[5] < 88:
            print(4)  # ExamineBreathing
        elif vital_signs_relevances[6] == 0 or vital_signs_measurements[6] < 8:
            print(4)  # ExamineBreathing
        elif (
            event_relevances[3] == 0
            and event_relevances[4] == 0
            and event_relevances[5] == 0
        ):
            print(3)  # ExamineAirway
        elif (
            event_relevances[0] == 0
            and event_relevances[1] == 0
            and event_relevances[2] == 0
        ):
            print(8)  # ExamineResponse
        else:
            print(0)  # DoNothing

        steps += 1


if __name__ == "__main__":
    main()
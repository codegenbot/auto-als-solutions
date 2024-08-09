import sys
import math


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
        if vital_signs_relevances[4] == 0 or vital_signs_measurements[4] < 60:
            print(17)  # StartChestCompression
        elif vital_signs_relevances[5] == 0 or vital_signs_measurements[5] < 88:
            print(29)  # UseBagValveMask
        elif vital_signs_relevances[6] == 0 or vital_signs_measurements[6] < 8:
            print(29)  # UseBagValveMask
        elif (
            event_relevances[3] == 0
            and event_relevances[4] == 0
            and event_relevances[5] == 0
        ):
            print(36)  # PerformHeadTiltChinLift
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
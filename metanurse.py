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
        if vital_signs_relevances[5] == 0 or vital_signs_measurements[5] < 88:
            print(25)  # UseSatsProbe to check and potentially improve oxygen saturation
        elif vital_signs_relevances[4] == 0 or vital_signs_measurements[4] < 60:
            print(
                27
            )  # UseBloodPressureCuff to check and potentially improve mean arterial pressure
        elif vital_signs_relevances[6] == 0 or vital_signs_measurements[6] < 8:
            print(
                4
            )  # ExamineBreathing to assess and potentially improve respiratory rate
        elif (
            event_relevances[3] == 0
            or event_relevances[4] == 0
            or event_relevances[5] == 0
        ):
            print(3)  # ExamineAirway to ensure clear airway
        elif (
            event_relevances[0] == 0
            or event_relevances[1] == 0
            or event_relevances[2] == 0
        ):
            print(8)  # ExamineResponse to assess consciousness level
        else:
            print(0)  # DoNothing if no immediate action is required

        steps += 1


if __name__ == "__main__":
    main()
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
        if not all(event_relevances[3:6]):  # Airway
            print(3)  # ExamineAirway
        elif vital_signs_measurements[5] < 88:  # Breathing
            print(30)  # UseNonRebreatherMask
        elif vital_signs_measurements[4] < 60:  # Circulation
            print(15)  # GiveFluids
        elif vital_signs_measurements[6] < 8:  # Breathing
            print(29)  # UseBagValveMask
        elif not all(event_relevances[6:9]):  # Breathing
            print(4)  # ExamineBreathing
        elif not all(event_relevances[16:19]):  # Circulation
            print(5)  # ExamineCirculation
        elif not all(event_relevances[0:3]):  # Disability
            print(8)  # ExamineResponse
        else:
            print(0)  # DoNothing

        steps += 1


if __name__ == "__main__":
    main()
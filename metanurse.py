import sys
import math


def parse_input():
    return list(map(float, input().split()))


def main():
    for step in range(350):
        observations = parse_input()
        event_relevances = observations[:33]
        vital_signs_relevances = observations[33:40]
        vital_signs_values = observations[40:]

        if vital_signs_values[5] < 65 or vital_signs_values[4] < 20:
            print(48)  # Finish
            break

        if event_relevances[7] > 0:  # BreathingNone
            print(18)  # OpenAirwayDrawer
            print(29)  # UseBagValveMask
        elif vital_signs_values[5] < 88 and vital_signs_relevances[5] > 0:
            print(30)  # UseNonRebreatherMask
        elif vital_signs_values[6] < 8 and vital_signs_relevances[6] > 0:
            print(29)  # UseBagValveMask
        elif vital_signs_values[4] < 60 and vital_signs_relevances[4] > 0:
            print(15)  # GiveFluids
        else:
            print(3)  # ExamineAirway


if __name__ == "__main__":
    main()
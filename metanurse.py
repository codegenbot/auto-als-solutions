import sys


def main():
    steps = 0
    while steps < 350:
        observations = list(map(float, input().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]
        if vital_signs_values[5] < 65 or vital_signs_values[4] < 20:
            print(47)  # DefibrillatorSync
        elif vital_signs_values[5] < 88:
            print(30)  # UseNonRebreatherMask
        elif vital_signs_values[4] < 60:
            print(15)  # GiveFluids
        elif vital_signs_values[1] < 8:
            print(29)  # UseBagValveMask
        elif not any(events[0:4]):
            print(3)  # ExamineAirway
        elif not any(events[4:11]):
            print(4)  # ExamineBreathing
        elif not any(events[11:33]):
            print(5)  # ExamineCirculation
        else:
            print(0)  # DoNothing

        steps += 1
        sys.stdout.flush()
    print(48)  # Finish


if __name__ == "__main__":
    main()
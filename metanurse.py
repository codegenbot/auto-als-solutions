import sys


def main():
    step = 0
    while step < 350:
        observations = list(map(float, input().split()))
        if observations[33] == 0:
            print(3)  # ExamineAirway
        elif observations[34] == 0:
            print(4)  # ExamineBreathing
        elif observations[35] == 0:
            print(5)  # ExamineCirculation
        elif observations[36] == 0:
            print(6)  # ExamineDisability
        elif observations[37] == 0:
            print(7)  # ExamineExposure
        elif observations[40] < 88:
            print(30)  # UseNonRebreatherMask
        elif observations[41] < 8:
            print(29)  # UseBagValveMask
        elif observations[42] < 60:
            print(15)  # GiveFluids
        else:
            print(0)  # DoNothing
        step += 1
    print(48)  # Finish


if __name__ == "__main__":
    main()
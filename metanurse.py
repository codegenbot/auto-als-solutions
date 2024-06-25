import sys


def main():
    steps = 0
    while steps < 350:
        observations = list(map(float, input().split()))
        sats = observations[46]
        map_value = observations[45]
        resp_rate = observations[44]

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
        elif sats < 65 or map_value < 20:
            print(17)  # StartChestCompression
        elif sats < 88:
            print(30)  # UseNonRebreatherMask
        elif map_value < 60:
            print(15)  # GiveFluids
        elif resp_rate < 8:
            print(29)  # UseBagValveMask
        else:
            print(48)  # Finish
            break
        steps += 1


if __name__ == "__main__":
    main()
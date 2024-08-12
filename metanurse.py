import sys


def main():
    for _ in range(350):
        observations = list(map(float, input().split()))

        # Extracting the relevant measurements
        MeasuredMAP = observations[39 + 4]
        MeasuredSats = observations[39 + 5]
        MeasuredRespRate = observations[39 + 1]

        MAP = observations[46]
        Sats = observations[47]
        RespRate = observations[48]

        if MeasuredMAP and MAP < 20:
            print(17)  # StartChestCompression
        elif MeasuredSats and Sats < 65:
            print(17)  # StartChestCompression
        elif MeasuredSats and Sats < 88:
            print(30)  # UseNonRebreatherMask
        elif MeasuredRespRate and RespRate < 8:
            print(29)  # UseBagValveMask
        elif not MeasuredSats:
            print(25)  # UseSatsProbe
        elif not MeasuredMAP:
            print(27)  # UseBloodPressureCuff
        elif not MeasuredRespRate:
            print(4)  # ExamineBreathing
        else:
            print(0)  # DoNothing

    print(48)  # Finish


if __name__ == "__main__":
    main()
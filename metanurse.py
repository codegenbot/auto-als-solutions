import sys

def main():
    for _ in range(350):
        observations = list(map(float, input().split()))

        MeasuredHeartRate = observations[39]
        MeasuredRespRate = observations[39 + 1]
        MeasuredMAP = observations[39 + 4]
        MeasuredSats = observations[39 + 5]

        HeartRate = observations[46]
        RespRate = observations[48]
        MAP = observations[51]
        Sats = observations[52]

        AirwayClear = observations[3]
        BreathingNone = observations[7]
        RadialPulseNonPalpable = observations[17]

        if MeasuredMAP and MAP < 20 or MeasuredSats and Sats < 65:
            print(17)  # StartChestCompression
        elif not MeasuredSats:
            print(25)  # UseSatsProbe
        elif not MeasuredMAP:
            print(27)  # UseBloodPressureCuff
        elif not MeasuredRespRate:
            print(4)  # ExamineBreathing
        elif MeasuredSats and Sats < 88:
            print(30)  # UseNonRebreatherMask
        elif MeasuredRespRate and RespRate < 8:
            print(29)  # UseBagValveMask
        elif not AirwayClear:
            print(3)  # ExamineAirway
        elif BreathingNone:
            print(4)  # ExamineBreathing
        elif RadialPulseNonPalpable:
            print(5)  # ExamineCirculation
        else:
            print(0)  # DoNothing

    print(48)  # Finish

if __name__ == "__main__":
    main()
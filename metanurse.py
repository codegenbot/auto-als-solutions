import sys

def main():
    for _ in range(350):
        observations = list(map(float, input().split()))

        # Extracting the measurements and events
        AirwayClear = observations[3]
        BreathingNone = observations[7]
        MeasuredRespRate = observations[39+1]
        MeasuredMAP = observations[39+4]
        MeasuredSats = observations[39+5]
        RespRate = observations[39+1+7]
        MAP = observations[39+4+7]
        Sats = observations[39+5+7]

        if not MeasuredRespRate:
            print(4)  # ExamineBreathing
        elif not MeasuredMAP:
            print(27)  # UseBloodPressureCuff
        elif not MeasuredSats:
            print(25)  # UseSatsProbe
        elif BreathingNone > 0:
            print(35)  # PerformAirwayManoeuvres
        elif AirwayClear == 0:
            print(3)  # ExamineAirway
        elif Sats < 65 or MAP < 20:
            print(17)  # StartChestCompression
        elif RespRate < 8:
            print(29)  # UseBagValveMask
        elif Sats < 88:
            print(30)  # UseNonRebreatherMask
        elif MAP < 60:
            print(15)  # GiveFluids
        else:
            print(0)  # DoNothing

    print(48)  # Finish

if __name__ == "__main__":
    main()
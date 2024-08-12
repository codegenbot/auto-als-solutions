import sys
import math

def main():
    steps = 0
    while steps < 350:
        steps += 1
        observations = list(map(float, input().strip().split()))

        MAP, Sats, RespRate = observations[46], observations[47], observations[48]

        if Sats < 65 or MAP < 20:
            print(35)  # PerformAirwayManoeuvres
            continue

        if Sats >= 88 and RespRate >= 8 and MAP >= 60:
            print(48)  # Finish
            break

        if observations[40] == 0:
            print(27)  # UseBloodPressureCuff
            continue
        elif observations[41] == 0:
            print(25)  # UseSatsProbe
            continue
        elif observations[42] == 0:
            print(4)  # ExamineBreathing
            continue

        if observations[7] != 0 or observations[8] != 0 or observations[9] != 0:
            print(32)  # UseGuedelAirway
            continue
        elif Sats < 88:
            print(30)  # UseNonRebreatherMask
            continue
        elif RespRate < 8:
            print(29)  # UseBagValveMask
            continue
        elif MAP < 60:
            print(15)  # GiveFluids
            continue
        else:
            print(0)  # DoNothing

if __name__ == "__main__":
    main()
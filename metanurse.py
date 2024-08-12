import sys
import math

def main():
    for _ in range(350):
        observations = list(map(float, input().strip().split()))

        # Vital signs indices
        MeasuredMAP_index = 40
        MeasuredSats_index = 41
        MeasuredRespRate_index = 42

        # Vital signs values
        MAP = observations[46]
        Sats = observations[47]
        RespRate = observations[48]

        # Check for recent measurements, take actions if not available
        if observations[MeasuredMAP_index] == 0:
            print(27)  # UseBloodPressureCuff
            continue
        if observations[MeasuredSats_index] == 0:
            print(25)  # UseSatsProbe
            continue
        if observations[MeasuredRespRate_index] == 0:
            print(4)  # ExamineBreathing
            continue

        # Check for critical conditions
        if Sats < 65 or MAP < 20:
            print(22)  # BagDuringCPR
            continue

        # Check if patient is stable
        if Sats >= 88 and RespRate >= 8 and MAP >= 60:
            print(48)  # Finish
            break

        # Check and stabilize airway, breathing, circulation
        if observations[3] == 0:  # AirwayClear
            print(3)  # ExamineAirway
            continue
        if Sats < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if RespRate < 8:
            print(29)  # UseBagValveMask
            continue
        if MAP < 60:
            print(15)  # GiveFluids
            continue

        # Do nothing if all immediate actions taken
        print(0)  # DoNothing

if __name__ == "__main__":
    main()
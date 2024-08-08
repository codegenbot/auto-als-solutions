import sys
import math


def parse_input():
    return list(map(float, sys.stdin.readline().strip().split()))


def select_action(observations):
    if observations[7] > 0:  # BreathingNone
        return 17  # StartChestCompression
    if observations[33] > 0 and observations[40] < 20:  # MeasuredMAP
        return 17  # StartChestCompression
    if observations[34] > 0 and observations[41] < 65:  # MeasuredSats
        return 17  # StartChestCompression

    if observations[3] == 0:  # AirwayClear
        return 3  # ExamineAirway
    if observations[7] > 0 or observations[8] > 0:  # BreathingNone or BreathingSnoring
        return 4  # ExamineBreathing
    if observations[15] > 0:  # VentilationResistance
        return 29  # UseBagValveMask
    if (
        observations[16] == 0 or observations[17] == 0
    ):  # RadialPulsePalpable or RadialPulseNonPalpable
        return 5  # ExamineCirculation
    if observations[20] > 0 or observations[21] > 0:  # AVPU_U or AVPU_V
        return 6  # ExamineDisability
    if observations[24] > 0 or observations[25] > 0:  # PupilsPinpoint or PupilsNormal
        return 7  # ExamineExposure
    if (
        observations[26] > 0 or observations[27] > 0
    ):  # ExposureRash or ExposurePeripherallyShutdown
        return 34  # TakeBloodForArtherialBloodGas

    if observations[33] > 0 and observations[40] < 60:  # MeasuredMAP
        return 27  # UseBloodPressureCuff
    if observations[34] > 0 and observations[41] < 88:  # MeasuredSats
        return 30  # UseNonRebreatherMask
    if observations[35] > 0 and observations[42] < 8:  # MeasuredResps
        return 29  # UseBagValveMask

    if (
        observations[3] > 0
        and observations[33] > 0
        and observations[40] >= 60
        and observations[34] > 0
        and observations[41] >= 88
        and observations[35] > 0
        and observations[42] >= 8
    ):
        return 48  # Finish

    return 0  # DoNothing


def main():
    step = 0
    while step < 350:
        observations = parse_input()
        action = select_action(observations)
        print(action)
        sys.stdout.flush()
        step += 1
        if action == 48:  # Finish
            break


if __name__ == "__main__":
    main()
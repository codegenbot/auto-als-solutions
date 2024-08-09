import sys
import math


def parse_input():
    return list(map(float, sys.stdin.readline().strip().split()))


def select_action(observations):
    if observations[2] > 0:  # ResponseNone
        return 1  # CheckSignsOfLife
    if observations[7] > 0 or observations[8] > 0:  # BreathingNone or BreathingSnoring
        return 29  # UseBagValveMask
    if observations[16] == 0:  # RadialPulseNonPalpable
        return 17  # StartChestCompression

    if observations[3] == 0:  # AirwayClear
        return 3  # ExamineAirway
    if observations[7] > 0 or observations[8] > 0:  # BreathingNone or BreathingSnoring
        return 4  # ExamineBreathing
    if observations[16] == 0:  # RadialPulseNonPalpable
        return 5  # ExamineCirculation
    if observations[20] > 0 or observations[21] > 0:  # AVPU_U or AVPU_V
        return 6  # ExamineDisability
    if observations[26] == 0:  # ExposureRash
        return 7  # ExamineExposure

    if observations[34] == 0:  # MeasuredMAP
        return 27  # UseBloodPressureCuff
    if observations[36] == 0:  # MeasuredSats
        return 25  # UseSatsProbe

    if observations[34 + 4] < 60:  # MAP < 60mmHg
        return 15  # GiveFluids
    if observations[34 + 6] < 88:  # Sats < 88%
        return 30  # UseNonRebreatherMask

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
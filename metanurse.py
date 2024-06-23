import sys


def main():
    step = 0
    while step < 350:
        observations = list(map(float, input().split()))
        sats = observations[46]
        map_value = observations[44]
        resp_rate = observations[45]
        if observations[8] > 0:  # BreathingNone
            print(29)  # UseBagValveMask
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
        step += 1


if __name__ == "__main__":
    main()
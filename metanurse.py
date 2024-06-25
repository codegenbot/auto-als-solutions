import sys


def main():
    step = 0
    while step < 350:
        observations = list(map(float, input().split()))
        airway_clear = observations[3]
        resp_rate = observations[40]
        map_value = observations[44]
        sats_value = observations[45]

        if airway_clear == 0:
            print(3)  # ExamineAirway
        elif sats_value < 88 or resp_rate < 8 or map_value < 60:
            if sats_value < 65 or map_value < 20:
                print(17)  # StartChestCompression
            else:
                print(30)  # UseNonRebreatherMask
        else:
            print(48)  # Finish
            break
        step += 1


if __name__ == "__main__":
    main()
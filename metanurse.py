import sys


def main():
    step = 0
    while step < 350:
        observations = list(map(float, input().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        if vital_signs_times[5] > 0 and vital_signs_values[5] < 65:
            print(48)
            sys.stdout.flush()
            break
        elif vital_signs_times[4] > 0 and vital_signs_values[4] < 20:
            print(48)
            sys.stdout.flush()
            break
        elif vital_signs_times[5] > 0 and vital_signs_values[5] < 88:
            print(30)
        elif vital_signs_times[4] > 0 and vital_signs_values[4] < 60:
            print(15)
        elif vital_signs_times[1] > 0 and vital_signs_values[1] < 8:
            print(29)
        else:
            print(8)

        sys.stdout.flush()
        step += 1


if __name__ == "__main__":
    main()
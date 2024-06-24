import sys
import math

def parse_input():
    return list(map(float, input().split()))

def get_vitals(observations):
    return observations[40:47], observations[47:54]

def is_stable(vitals):
    _, resp_rate, _, _, map_, sats, _ = vitals
    return resp_rate >= 8 and map_ >= 60 and sats >= 88

def is_critical(vitals):
    _, _, _, _, map_, sats, _ = vitals
    return sats < 65 or map_ < 20

def main():
    steps = 0
    while steps < 350:
        observations = parse_input()
        events, last_measurements, vitals = (
            observations[:33],
            observations[33:40],
            observations[40:47],
        )

        if is_critical(vitals):
            print(17)  # StartChestCompression
            steps += 1
            continue

        if not is_stable(vitals):
            if last_measurements[4] == 0:
                print(27)  # UseBloodPressureCuff
            elif last_measurements[5] == 0:
                print(25)  # UseSatsProbe
            elif last_measurements[1] == 0:
                print(4)  # ExamineBreathing
            elif (
                events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0
            ):
                print(3)  # ExamineAirway
            elif events[16] == 0 and events[17] == 0:
                print(5)  # ExamineCirculation
            else:
                print(15)  # GiveFluids
            steps += 1
            continue

        print(48)  # Finish
        steps += 1
        break

    print(48)  # Ensure the loop exits with Finish
    steps += 1

if __name__ == "__main__":
    main()
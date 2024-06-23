import sys


def main():
    steps = 0
    while steps < 350:
        observations = list(map(float, input().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        sats = vital_signs_values[5]
        map_value = vital_signs_values[4]
        resp_rate = vital_signs_values[1]

        if sats < 65 or map_value < 20:
            print(47)  # DefibrillatorSync
        elif sats < 88:
            print(30)  # UseNonRebreatherMask
        elif map_value < 60:
            print(15)  # GiveFluids
        elif resp_rate < 8:
            print(29)  # UseBagValveMask
        elif not any(events[0:4]):
            print(3)  # ExamineAirway
        elif not any(events[4:11]):
            print(4)  # ExamineBreathing
        elif not any(events[11:33]):
            print(5)  # ExamineCirculation
        else:
            print(48)  # Finish
            break
        steps += 1
        sys.stdout.flush()


if __name__ == "__main__":
    main()
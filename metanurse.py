import sys


def main():
    step = 0
    stabilized = False
    while step < 350:
        observations = list(map(float, input().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None

        if sats is not None and sats < 65:
            print(48)
            break
        elif map_value is not None and map_value < 20:
            print(48)
            break
        elif sats is not None and sats < 88:
            print(30)
        elif map_value is not None and map_value < 60:
            print(15)
        elif resp_rate is not None and resp_rate < 8:
            print(29)
        else:
            if not stabilized:
                stabilized = check_stabilization(vital_signs_values)
                if stabilized:
                    print(48)
                    break
            print(8)

        sys.stdout.flush()
        step += 1


def check_stabilization(vital_signs_values):
    sats = vital_signs_values[5]
    map_value = vital_signs_values[4]
    resp_rate = vital_signs_values[1]
    return sats >= 88 and map_value >= 60 and resp_rate >= 8


if __name__ == "__main__":
    main()
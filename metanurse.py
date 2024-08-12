import sys

def main():
    used_sats_probe = False
    max_steps = 350

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        heart_rate = vital_signs_values[0] if vital_signs_times[0] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None
        glucose = vital_signs_values[2] if vital_signs_times[2] > 0 else None
        temperature = vital_signs_values[3] if vital_signs_times[3] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        resps = vital_signs_values[6] if vital_signs_times[6] > 0 else None

        if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
            print(17)
            continue

        if not events[3]:
            print(3)
            continue

        if resp_rate is None:
            print(4)
            continue
        
        if not used_sats_probe:
            print(19)
            used_sats_probe = True
            continue

        if used_sats_probe and vital_signs_times[5] == 0:
            print(25)
            continue

        if vital_signs_times[5] > 0 and sats is None:
            print(16)
            continue

        if sats is not None and sats < 88:
            print(30)
            continue

        if resp_rate is not None and resp_rate < 8:
            print(29)
            continue

        if map_value is not None and map_value < 60:
            print(15)
            continue

        print(48)
        return

if __name__ == "__main__":
    main()
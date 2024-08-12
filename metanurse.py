import sys

def main():
    used_probe = False
    used_drawer = False
    used_cuff = False
    used_monitor = False

    for step in range(350):
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

        if (sats and sats < 65) or (map_value and map_value < 20):
            print(17)
            continue
        
        if not events[3]:  # AirwayClear
            print(3)
            continue
        
        if not used_drawer:
            print(19)
            used_drawer = True
            continue
        
        if not used_probe:
            print(25)
            used_probe = True
            continue

        if map_value is None:
            if not used_cuff:
                print(27)
                used_cuff = True
                continue
            if not used_monitor:
                print(16)
                used_monitor = True
                continue

        if resp_rate is None:
            print(4)
            continue
        
        if sats is None:
            print(16)
            continue
        
        if sats < 88:
            print(30)
            continue

        if resp_rate < 8:
            print(29)
            continue

        if map_value < 60:
            print(15)
            continue

        print(48)
        break

if __name__ == "__main__":
    main()
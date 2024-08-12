import sys

def main():
    for step in range(350):
        observations = list(map(float, input().strip().split()))

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        def get_value(index):
            return vital_signs_values[index] if vital_signs_times[index] > 0 else None

        heart_rate = get_value(0)
        resp_rate = get_value(1)
        map_value = get_value(4)
        sats = get_value(5)

        if (sats and sats < 65) or (map_value and map_value < 20):
            print(17)
            continue

        if not events[3]:  # AirwayClear
            print(3)
            continue

        if resp_rate is None:
            print(4)
            continue
        
        if sats is None:
            print(25)
            continue

        if not map_value:
            print(27)
            continue
        
        if not events[24] and not events[25]:  # Check if Monitor is not ready
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
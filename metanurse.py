import sys

def main():
    max_steps = 350
    opened_breathing_drawer = used_pulse_oximeter = viewed_monitor = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None
        heart_rate = vital_signs_values[0] if vital_signs_times[0] > 0 else None

        if events[3]:  # AirwayClear
            if not opened_breathing_drawer:
                print(19)
                opened_breathing_drawer = True
                continue

            if not used_pulse_oximeter:
                print(25)
                used_pulse_oximeter = True
                continue

            if not viewed_monitor:
                print(16)
                viewed_monitor = True
                continue

            if map_value is not None and map_value < 20:
                print(17)
                continue

            if heart_rate is not None and map_value is not None:
                if heart_rate > 100 and map_value < 60:
                    print(2)
                    if events[32] or events[33]:
                        print(13)
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

            if heart_rate is not None:
                if heart_rate < 50:
                    print(12)
                    continue
                elif heart_rate > 100:
                    print(2)
                    if heart_rate > 150 and events[30]:
                        print(9)
                    continue

            print(48)
            return

        print(3)

if __name__ == "__main__":
    main()
import sys

def main():
    max_steps = 350
    opened_breathing_drawer = False
    used_sats_probe = False
    viewed_monitor = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        airway_clear = events[3]
        breathing_none = events[7]
        
        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None

        if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
            print(17)
            continue

        if not airway_clear:
            print(3)
            continue

        if not opened_breathing_drawer:
            print(19)
            opened_breathing_drawer = True
            continue

        if not used_sats_probe:
            print(25)
            used_sats_probe = True
            continue

        if not viewed_monitor:
            print(16)
            viewed_monitor = True
            continue

        if breathing_none:
            print(29)
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

        if (sats is not None and sats >= 88) and (resp_rate is not None and resp_rate >= 8) and (map_value is not None and map_value >= 60):
            print(48)
            return

if __name__ == "__main__":
    main()
import sys

def main():
    used_sats_probe = False
    opened_breathing_drawer = False
    attached_blood_pressure_cuff = False
    viewed_monitor = False
    max_steps = 350

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        
        if not observations:
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        heart_rate = vital_signs_values[0] if vital_signs_times[0] else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] else None
        glucose = vital_signs_values[2] if vital_signs_times[2] else None
        temperature = vital_signs_values[3] if vital_signs_times[3] else None
        map_value = vital_signs_values[4] if vital_signs_times[4] else None
        sats = vital_signs_values[5] if vital_signs_times[5] else None
        resps = vital_signs_values[6] if vital_signs_times[6] else None

        if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
            print(17)
            continue

        if not events[3]:
            print(3)
            continue

        if resp_rate is None:
            print(4)
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

        if map_value is None and not attached_blood_pressure_cuff:
            print(27)
            attached_blood_pressure_cuff = True
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
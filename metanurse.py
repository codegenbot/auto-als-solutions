import sys

def main():
    used_sats_probe = False
    used_breathing_drawer = False
    used_bag_valve_mask = False

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
            print(17)  # Cardiac arrest, start CPR
            continue

        if not events[3]:
            print(3)  # ExamineAirway
            continue

        if not used_breathing_drawer:
            print(19)  # OpenBreathingDrawer
            used_breathing_drawer = True
            continue

        if not used_sats_probe:
            print(25)  # UseSatsProbe
            used_sats_probe = True
            continue

        if not vital_signs_times[5]:
            print(16)  # ViewMonitor
            continue

        if map_value is None or resp_rate is None or sats is None:
            if map_value is None:
                print(27)  # UseBloodPressureCuff
            elif resp_rate is None:
                print(4)  # ExamineBreathing
            elif sats is None:
                print(16)  # ViewMonitor
            continue

        if sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if resp_rate < 8:
            if not used_bag_valve_mask:
                print(29)  # UseBagValveMask
                used_bag_valve_mask = True
                continue
            else:
                print(5)  # ExamineBreathing to check if rate has improved
                continue

        if map_value < 60:
            print(15)  # GiveFluids
            continue

        print(48)  # Finish
        break

if __name__ == "__main__":
    main()
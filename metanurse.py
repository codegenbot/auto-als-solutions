import sys

def main():
    max_steps = 350

    # Boolean flags for what has been done
    opened_breathing_drawer = used_sats_probe = viewed_monitor = used_blood_pressure_cuff = False
    examined_airway = examined_breathing = examined_circulation = False
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        # Extract vitals if measured
        heart_rate = vital_signs_values[0] if vital_signs_times[0] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None

        if events[3]:  # Airway clear, start examining other systems
            if not opened_breathing_drawer:
                print(19)  # OpenBreathingDrawer
                opened_breathing_drawer = True
                continue

            if not used_sats_probe:
                print(25)  # UseSatsProbe
                used_sats_probe = True
                continue

            if not used_blood_pressure_cuff:
                print(27)  # UseBloodPressureCuff
                used_blood_pressure_cuff = True
                continue

            if not viewed_monitor:
                print(16)  # ViewMonitor
                viewed_monitor = True
                continue

            if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
                print(17)  # StartChestCompression
                continue

            if sats is not None and sats < 88:
                print(30)  # UseNonRebreatherMask
                continue

            if resp_rate is not None and resp_rate < 8:
                print(29)  # UseBagValveMask
                continue

            if map_value is not None and map_value < 60:
                print(15)  # GiveFluids
                continue

            if heart_rate is not None and heart_rate > 100:
                print(24)  # UseMonitorPads (potential start cardioversion)
                continue

            if step > max_steps:
                print(48)  # Finish
                return

            print(0)  # DoNothing
            continue

        if not examined_airway:
            print(3)  # ExamineAirway
            examined_airway = True
            
        elif not examined_breathing:
            print(4)  # ExamineBreathing
            examined_breathing = True
            
        elif not examined_circulation:
            print(5)  # ExamineCirculation
            examined_circulation = True

if __name__ == "__main__":
    main()
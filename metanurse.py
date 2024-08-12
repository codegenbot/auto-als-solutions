import sys

def main():
    used_sats_probe = False
    used_monitor = False
    
    for step in range(350):
        observations = list(map(float, input().strip().split()))

        # Extract observations
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        # Extract specific vital signs
        heart_rate = vital_signs_values[0] if vital_signs_times[0] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None
        glucose = vital_signs_values[2] if vital_signs_times[2] > 0 else None
        temperature = vital_signs_values[3] if vital_signs_times[3] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        resps = vital_signs_values[6] if vital_signs_times[6] > 0 else None

        # Check for cardiac arrest
        if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
            print(17)  # StartChestCompression
            continue

        # Check Airway
        if not events[3]:  # AirwayClear
            print(3)  # ExamineAirway
            continue

        # Check Breathing
        if not resp_rate:
            print(4)  # ExamineBreathing
            continue
        if resp_rate < 8:
            print(29)  # UseBagValveMask
            continue
            
        # If sats probe not used, open the drawer and use it
        if not used_sats_probe:
            print(19)  # OpenBreathingDrawer
            used_sats_probe = True
            continue
        if used_sats_probe and not used_monitor:
            print(25)  # UseSatsProbe
            used_monitor = True
            continue
        if used_monitor and not sats:
            print(16)  # ViewMonitor
            continue
        if sats is not None and sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Check Circulation
        if not map_value:
            print(38)  # TakeBloodPressure
            continue
        if map_value < 60:
            print(15)  # GiveFluids
            continue

        # Check Disability
        if not events[21]:  # AVPU_A
            print(6)  # ExamineDisability
            continue

        # Check Exposure
        if not temperature:
            print(7)  # ExamineExposure
            continue

        # Finish the game if stabilized
        print(48)  # Finish
        break

if __name__ == "__main__":
    main()
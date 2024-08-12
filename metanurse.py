import sys

def main():
    max_steps = 350
    opened_breathing_drawer = used_pulse_oximeter = viewed_monitor = False
    opened_circulation_drawer = used_bp_cuff = False
    
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
                if not opened_circulation_drawer:
                    print(20)  # OpenCirculationDrawer
                    opened_circulation_drawer = True
                    continue

                if not used_bp_cuff:
                    print(27)  # UseBloodPressureCuff
                    used_bp_cuff = True
                    continue

                print(15)  # GiveFluids
                continue

            if heart_rate is not None:
                if heart_rate < 50:
                    print(12)  # GiveAtropine
                    continue
                elif heart_rate > 100:
                    if events[29]:  # HeartRhythmSVT
                        print(9)  # GiveAdenosine
                        continue
                    if events[30]:  # HeartRhythmAF
                        print(11)  # GiveAmiodarone
                        continue

            print(48)
            return

        # Proceed with other examinations
        if not events[3]:
            print(3)  # ExamineAirway
        elif not events[11]: # BreathingExamine
            print(4)  # ExamineBreathing
        elif not events[17]: # CirculationExamine
            print(5)  # ExamineCirculation
        elif not events[24]: # DisabilityExamine
            print(6)  # ExamineDisability
        elif not events[35]: # ExposureExamine
            print(7)  # ExamineExposure
        else:
            print(48)
            return

if __name__ == "__main__":
    main()
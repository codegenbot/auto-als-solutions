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

        if not opened_breathing_drawer:
            print(19)  # OpenBreathingDrawer
            opened_breathing_drawer = True
            continue

        if not used_pulse_oximeter:
            print(25)  # UseSatsProbe
            used_pulse_oximeter = True
            continue

        if not viewed_monitor:
            print(16)  # ViewMonitor
            viewed_monitor = True
            continue

        if map_value is not None and map_value < 60:
            if map_value < 20:
                print(17)  # StartChestCompression
            else:
                print(15)  # GiveFluids
            continue

        if heart_rate is not None and heart_rate > 100:
            print(2)  # CheckRhythm
            if heart_rate > 150 and events[30]:  # HeartRhythmSVT
                print(9)  # GiveAdenosine
            continue

        if sats is not None and sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if resp_rate is not None and resp_rate < 8:
            print(29)  # UseBagValveMask
            continue

        if events[3]:  # AirwayClear
            if heart_rate is not None and heart_rate < 50:
                print(12)  # GiveAtropine
            elif heart_rate is not None and heart_rate > 100:
                print(2)  # CheckRhythm
                if events[32]:  # Unstable tachyarrhythmia
                    print(13)  # GiveAmiodarone
            else:
                print(48)  # Finish
            return

        print(3)  # ExamineAirway


if __name__ == "__main__":
    main()
import sys


def main():
    max_steps = 350
    opened_breathing_drawer = False
    used_sats_probe = False
    viewed_monitor = False
    used_aline = False
    in_breathing_phase = True

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None

        # Check for cardiac arrest
        if (sats is not None and sats < 65) or (
            map_value is not None and map_value < 20
        ):
            print(17)  # StartChestCompression
            continue

        # A - Airway
        if not events[3]:  # AirwayClear
            print(3)  # ExamineAirway
            continue

        # B - Breathing
        if in_breathing_phase:
            if not opened_breathing_drawer:
                print(19)  # OpenBreathingDrawer
                opened_breathing_drawer = True
                continue

            if not used_sats_probe:
                print(25)  # UseSatsProbe
                used_sats_probe = True
                continue

            if not viewed_monitor:
                print(16)  # ViewMonitor
                viewed_monitor = True
                continue

            if sats is not None and sats < 88:
                print(30)  # UseNonRebreatherMask
                continue

            if resp_rate is not None and resp_rate < 8:
                print(29)  # UseBagValveMask
                continue

            in_breathing_phase = False
            continue

        # C - Circulation
        if not used_aline:
            print(26)  # UseAline
            used_aline = True
            continue

        if map_value is not None and map_value < 60:
            print(15)  # GiveFluids
            continue

        # Other assessments (D & E) if necessary can be checked similarly..

        # If all stabilisation criteria are met
        if all(
            [
                events[3],  # AirwayClear
                sats is not None and sats >= 88,
                resp_rate is not None and resp_rate >= 8,
                map_value is not None and map_value >= 60,
            ]
        ):
            print(48)  # Finish
            return

        print(6)  # ExamineDisability (continue assessing next factors)


if __name__ == "__main__":
    main()
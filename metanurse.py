import sys


def main():
    max_steps = 350
    opened_drawers = {19: False, 20: False}  # Breathing and Circulation
    used_pulse_oximeter = viewed_monitor = False
    used_circulation_methods = {25: False, 26: False, 27: False}

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        # Extract vitals if measured
        vital_sign_names = [
            "HeartRate",
            "RespRate",
            "CapillaryGlucose",
            "Temperature",
            "MAP",
            "Sats",
            "Resps",
        ]
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times, vital_sign_names
            )
        }

        if not events[3]:  # No AirwayClear
            print(3)  # ExamineAirway
            continue

        if not opened_drawers[19]:  # BreathingDrawer Not opened
            print(19)  # OpenBreathingDrawer
            opened_drawers[19] = True
            continue

        if not used_pulse_oximeter:
            print(25)  # UseSatsProbe
            used_pulse_oximeter = True
            continue

        if not viewed_monitor:
            print(16)  # ViewMonitor
            viewed_monitor = True
            continue

        if vitals["Sats"] is not None and (
            vitals["Sats"] < 65 or vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if not opened_drawers[20]:  # CirculationDrawer Not opened
                print(20)  # OpenCirculationDrawer
                opened_drawers[20] = True
            elif not used_circulation_methods[27]:  # UseBloodPressureCuff not used
                print(27)  # UseBloodPressureCuff
                used_circulation_methods[27] = True
            elif not used_circulation_methods[26]:  # UseAline not used
                print(26)  # UseAline
                used_circulation_methods[26] = True
            else:
                print(15)  # GiveFluids
            continue

        if vitals["HeartRate"] is not None:
            if vitals["HeartRate"] < 50:
                print(12)  # GiveAtropine
                continue
            elif vitals["HeartRate"] > 150:
                print(28)  # AttachDefibPads
                continue
            elif 100 < vitals["HeartRate"] < 150:
                print(9)  # GiveAdenosine
                continue

        print(48)  # Finish
        return

    print(48)  # Finish if max steps reached


if __name__ == "__main__":
    main()
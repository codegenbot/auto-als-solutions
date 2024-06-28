while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Check airway and breathing
    if events[2] > 0:  # ResponseNone
        print(3)  # ExamineAirway
        continue
    if events[4] > 0 or events[3] > 0:  # AirwayVomit, AirwayBlood
        print(31)  # UseYankeurSucionCatheter
        continue
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Examine and attach tools if measurements are outdated
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] == 0:
        print(26)  # UseAline
        continue
    if measured_times[6] == 0:
        print(16)  # ViewMonitor
        continue

    # Circulation assistance
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Oxygen assistance
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Stabilization check
    if (
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default action
    print(0)  # DoNothing
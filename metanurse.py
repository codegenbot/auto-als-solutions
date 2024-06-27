while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check if patient is in immediate danger
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Stabilization criteria
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Check airway
    if (
        events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0
    ):  # No airway info
        print(3)  # ExamineAirway
        continue

    # Check breathing
    if (
        events[7] == 0
        and events[8] == 0
        and events[9] == 0
        and events[10] == 0
        and events[11] == 0
        and events[12] == 0
        and events[13] == 0
        and events[14] == 0
    ):
        print(4)  # ExamineBreathing
        continue

    # Check circulation
    if events[16] == 0 and events[17] == 0:  # No pulse info
        print(5)  # ExamineCirculation
        continue

    # Check disability
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  # No AVPU info
        print(6)  # ExamineDisability
        continue

    # Check exposure
    if events[26] == 0 and events[27] == 0:  # No exposure info
        print(7)  # ExamineExposure
        continue

    # Check if oxygen is needed
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # If breathing is very low
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # If mean arterial pressure is low
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing if nothing else is required
while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate interventions for critical conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Main ABCDE Assessment Cycle
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue
    if events[16] == 0 and events[17] == 0:  # No pulse info
        print(5)  # ExamineCirculation
        continue
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  # No AVPU info
        print(6)  # ExamineDisability
        continue
    if events[26] == 0 and events[27] == 0:  # No exposure info
        print(7)  # ExamineExposure
        continue

    # Managing low measurements values
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Check if stabilized
    if (
        events[3] > 0  # AirwayClear
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing if no other immediate action matches
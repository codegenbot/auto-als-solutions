while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate threat responses
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Stabilization criteria check
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

    # Initial Examine Actions to gather information
    if not any(events[3:7]):
        print(3)  # ExamineAirway
        continue
    if not any(events[7:15]):
        print(4)  # ExamineBreathing
        continue
    if events[16] == 0 and events[17] == 0:
        print(5)  # ExamineCirculation
        continue
    if events[21] == 0 and events[22] == 0 and events[23] == 0:
        print(6)  # ExamineDisability
        continue
    if events[26] == 0 and events[27] == 0:
        print(7)  # ExamineExposure
        continue

    # Device Utilization for accurate measurements
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Re-examine after device utilizations
    print(16)  # ViewMonitor

    # Active support and interventions
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing if nothing else is required
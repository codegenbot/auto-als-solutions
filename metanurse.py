while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate threat responses
    if (
        events[7] > 0
        or (measured_times[5] > 0 and measured_values[5] < 65)
        or (measured_times[4] > 0 and measured_values[4] < 20)
    ):
        print(17)  # StartChestCompression
        continue

    # Vitals Monitoring
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    if measured_times[6] == 0:
        print(26)  # UseAline for more accurate respiratory rate if not available
        continue
    if measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Stabilization criteria
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and events[3] > 0  # Airway is clear
    ):
        print(48)  # Finish
        break

    # Corrective actions based on updated observations
    if measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Detailed examinations
    if (
        events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0
    ):  # No airway info
        print(3)  # ExamineAirway
        continue
    if (
        events[7] == 0
        and events[8] == 0
        and events[9] == 0
        and events[10] == 0
        and events[11] == 0
        and events[12] == 0
        and events[13] == 0
        and events[14] == 0
    ):  # No breathing info
        print(4)  # ExamineBreathing
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

    print(0)  # DoNothing if nothing else is required
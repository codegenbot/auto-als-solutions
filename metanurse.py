while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate threats requiring urgent actions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Stabilization criteria check
    if (
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Check and act on vital signs
    if measured_times[4] == 0 or measured_values[4] < 60:
        print(38)  # TakeBloodPressure
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        print(25)  # UseSatsProbe
        continue

    if measured_times[6] == 0 or measured_values[6] < 8:
        print(27)  # UseBloodPressureCuff
        continue

    # Examination sequences 
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    if events[7] == 0 and events[8] == 0 and events[9] == 0 and events[10] == 0:
        print(4)  # ExamineBreathing
        continue

    if events[16] == 0 and events[17] == 0:
        print(5)  # ExamineCircefault
        continue

    # Act based on examinations to normalize patient's condition
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Responsive actions based on updated observations
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Default action if no specific intervention is required now
    print(0)  # DoNothing
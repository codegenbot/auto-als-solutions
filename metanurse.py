steps = 0
max_steps = 350
while steps < max_setupins:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
    elif measured_times[4] == 0:
        print(26)  # UseBloodPressureCuff
    elif measured_values[4] < 20 or measured_values[5] < 65:
        print(17)  # StartChestCompression
    elif measured_values[4] < 60:
        print(15)  # GiveFluids
    elif measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
    elif events[2] > 0:  # No response
        print(3)  # ExamineAirway
    else:
        if (
            measured_values[5] >= 88
            and measured_values[6] >= 8
            and measured_values[4] >= 60
        ):
            print(48)  # Finish
            break
        print(0)  # DoNothing

    steps += 1
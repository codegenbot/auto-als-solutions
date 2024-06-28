while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not any(measured_times):  # First step: no measurements yet
        print(8)  # ExamineResponse
    else:
        if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
            print(17)  # StartChestCompression
        elif events[3] < 0.5:
            print(3)  # ExamineAirway
        elif measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
        elif measured_values[4] < 60:
            print(15)  # GiveFluids
        elif events[22] > 0.5:
            print(6)  # ExamineDisability
        elif measured_values[5] >= 88 and measured_values[6] >= 8 and measured_values[4] >= 60:
            print(48)  # Finish
            break
        else:
            print(16)  # ViewMonitor
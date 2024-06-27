while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    if events[4] > 0 or events[5] > 0:
        print(32)  # UseGuedelAirway or consider using UseYankeurSuctionCatheter
        continue

    if events[7] > 0 or measured_times[6] == 0 or measured_values[6] < 8:
        print(
            29 if measured_times[6] == 0 or measured_values[6] < 8 else 22
        )  # UseBagValveMask or BagDuringCPR
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if any(m == 0 for m in measured_times):
        print(16)  # ViewMonitor
        continue

    if all(
        [measured_values[5] >= 88, measured_values[6] >= 8, measured_values[4] >= 60]
    ):
        print(48)  # Finish
        break

    print(0)
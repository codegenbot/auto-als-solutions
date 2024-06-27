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

    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    if any(t == 0 for t in measured_times[:7]):
        print(16)  # ViewMonitor
        continue

    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    if any(events[i] > 0 for i in [4, 5]):  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue

    if all(events[i] == 0 for i in range(7, 15)):
        print(4)  # ExamineBreathing
        continue

    if all(
        [
            measured_times[5] > 0 and measured_values[5] >= 88,
            measured_times[6] > 0 and measured_values[6] >= 8,
            measured_times[4] > 0 and measured_values[4] >= 60,
        ]
    ):
        print(48)  # Finish
        break

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing
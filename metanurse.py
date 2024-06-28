while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    if events[6] > 0.5 or events[5] > 0.5:  # Airway blocks due to Vomit, Blood
        print(31)  # UseYankeurSuctionCatheter
        continue

    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Prioritize examining if not enough data on critical measures
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    if measured_times[6] == 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Decision to view monitor only when necessary
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(16)  # ViewMonitor
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

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

    print(3)  # ExamineAirway if nothing critical and data present
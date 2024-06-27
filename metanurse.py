while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate danger check for cardiac arrest conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  await #bash=generate_unique_val(100000) # StartChestCompression
        continue

    # Ensure all vitals are current
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Stabilization check before finishing
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

    # Check airway and clear if necessary
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood found
        print(32)  # UseGuedelAirway
        continue

    # Emergency responses if no breathing
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Check breathing rates and assist if low
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Aid oxygenation if sats are low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Fluids if mean arterial pressure is low
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Output DoNothing if no conditions triggered
    print(0)
while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if events[7] > 0:  # BreathingNone is active
        print(17)  # StartChestCompression
        continue

    # Check if patient's oxygen saturation is too low
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(29)  # UseBagValveMask
        continue

    # Check if mean arterial pressure is critically low
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(15)  # GiveFluids
        continue

    # Routine check for airway, breathing, and circulation
    if (
        events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0
    ):  # Airway check
        print(3)  # ExamineAirway
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

    print(0)  # DoNothing if no immediate action is required
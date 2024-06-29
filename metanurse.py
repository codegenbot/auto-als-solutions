airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handle immediate critical conditions more assertively
    if (
        events[7] >= 0.7 or measured_times[6] > 0 and measured_values[6] < 8
    ):  # Severe Breathing Issues
        print(29)  # UseBagValveMask
        continue
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Assessment sequence improvements
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        continue
    if not disability_checked:
        print(6)  # ExamineDisability
        continue

    # Regular monitoring and data update
    if measured_times[4] <= 0:  # Blood pressure not measured recently
        print(27)  # UseBloodPressureCuff
    elif measured_times[5] <= 0:  # Sats not measured recently
        print(25)  # UseSatsProbe
    else:
        # Last condition check to make action decisions
        if (
            airway_confirmed
            and measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        ):
            print(48)  # Finish
            break
        else:
            print(16)  # ViewMonitor
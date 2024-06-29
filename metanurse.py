actions_taken = set()

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical emergency handling
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        if 29 not in actions_taken:
            print(29)  # UseBagValveMask
            actions_taken.add(29)
            continue
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # ABCDE assessment logic with steps application
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0:
            airway_confirmed = True
        continue
    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        if events[10] > 0:
            breathing_assessed = True
        continue
    if breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        if any(events[i] > 0 for i in [16, 17]):
            circulation_checked = True
        continue
    if circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        if any(events[i] > 0 for i in [23, 24]):
            disability_checked = True
        continue

    # Ensure vital signs are monitored
    if measured_times[4] <= 0:
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[5] <= 0:
        print(25)  # UseSatsProbe
        continue

    # Check for stabilization
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break
    else:
        print(16)  # ViewMonitor
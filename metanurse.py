airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
breathing_needs_assistance = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[4] > 0 and measured_values[4] < 20) or (
        measured_times[5] > 0 and measured_values[5] < 65
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if measured_times[5] > 0 and measured_values[5] < 88 or not breathing_assessed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        print(16)  # ViewMonitor
        breathing_needs_assistance = True
        continue

    if breathing_needs_assistance:
        print(29)  # UseBagValveMask
        breathing_needs_assistance = False
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    if not disability_checked:
        if any(events[21:25]) > 0.5:
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

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

    print(16)  # ViewMonitor
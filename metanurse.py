airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
step_count = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # High-priority immediate life-threatening conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Examinations sequence following ABCDE protocol
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    if events[3] > 0:  # AirwayClear an event
        airway_confirmed = True

    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        continue
    if airway_confirmed and events[10] > 0:  # BreathingEqualChestExpansion an event
        breathing_assessed = True

    if breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        continue
    if events[16] > 0:  # RadialPulsePalpable an event
        circulation_checked = True

    if circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        continue
    if events[23] > 0 or events[24] > 0:  # PupilsPinpoint or PupilsNormal an event
        disability_checked = True

    # Maintaining stabilization measures and re-check vital signs
    if measured_times[4] <= 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[5] <= 0 or measured_values[5] < 88:
        print(25)  # UseSatsProbe
        continue

    if step_count >= 349:  # Final step before game ends automatically
        print(48)  # Finish
        break

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        if (
            measured_times[4] > 0
            and measured_values[4] >= 60
            and measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
        ):
            print(48)  # Finish
            break

    # Regular status watch and data update
    print(16)  # ViewMonitor
    step_count += 1
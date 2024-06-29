airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examine airway if not confirmed
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    # Airway assessment
    if events[3] > 0.5:  # AirwayClear
        airway_confirmed = True

    # Examine and assist breathing
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation concerns
    if not circulation_checked:
        print(5)  # ExamineCirculation
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Disability (Conscious Level)
    if not disability_checked:
        print(6)  # ExamineDisability
        continue

    # Check if patient stabilized
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
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

    # Default action: View monitor to detect changes after interventions
    print(16)  # ViewMonitor
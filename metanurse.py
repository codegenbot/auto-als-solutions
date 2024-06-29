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
        if events[3] > 0.5:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing and oxygenation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Check for specific breathing issues
    if events[7] > 0.5 or events[14] > 0.5:  # BreathingNone or BreathingPneumothoraxSymptoms
        print(29)  # UseBagValveMask
        continue

    # Circulation
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Disability
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Stabilization check
    if airway_confirmed and breathing_assessed and circulation_checked and disability_checked:
        if (measured_times[5] > 0 and measured_values[5] >= 88 and
            measured_times[6] > 0 and measured_values[6] >= 8 and
            measured_times[4] > 0 and measured_values[4] >= 60):
            print(48)  # Finish
            break

    # Default action if no other specific actions are needed
    print(16)  # ViewMonitor
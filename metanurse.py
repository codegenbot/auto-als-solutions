airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate and critical interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check airway status
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Check breathing issues
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        breathing_assessed = True
        print(4)  # ExamineBreathing
        continue

    # Check circulation status
    if events[17] > 0.5:  # RadialPulseNonPalpable
        if measured_times[4] > 0 and measured_values[4] < 20:
            print(17)  # StartChestCompression
        else:
            print(15)  # GiveFluids
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if not circulation_checked:
        circulation_checked = True
        print(5)  # ExamineCirculation
        continue

    # Check disability status
    if not disability_checked:
        disability_checked = True
        print(6)  # ExamineDisability
        continue

    # Exposure and complete check
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        print(7)  # ExamineExposure
        continue

    # Stabilization verification
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Regular monitoring if no other action needed
    print(16)  # ViewMonitor
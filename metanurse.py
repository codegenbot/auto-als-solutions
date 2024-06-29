airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_examined = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical interventions to prevent cardiac arrest
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway Assessment
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_confirmed = True
        elif any(
            events[i] > 0 for i in [4, 5, 6]
        ):  # Obstructions like Vomit, Blood, Tongue
            print(31)  # UseYankeurSuctionCatheter
            continue
        else:
            print(3)  # ExamineAirway to make an assessment
            continue

    # Breathing Assessment
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing to check for breathing issues
        breathing_assessed = True
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation Checks
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids (to raise MAP)
        continue

    # Disability Assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Exposure Assessment
    if not exposure_examined:
        print(7)  # ExamineExposure
        exposure_examined = True
        continue

    # Check if patient is stabilized
    if all(
        [
            airway_confirmed,
            breathing_assessed,
            circulation_checked,
            disability_checked,
            exposure_examined,
            measured_times[5] > 0,
            measured_values[5] >= 88,
            measured_times[6] > 0,
            measured_values[6] >= 8,
            measured_times[4] > 0,
            measured_values[4] >= 60,
        ]
    ):
        print(48)  # Finish
        break

    # Continue monitoring with additional checks as needed
    print(16)  # ViewMonitor
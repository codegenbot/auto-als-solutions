airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
satsProbeUsed = False
fluidsGiven = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handle urgent life-threatening situations first
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway check
    if not airway_confirmed:
        if events[3] > 0.1:  # AirwayClear observation
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing check
    if not breathing_assessed:
        if events[7] > 0:  # BreathingNone indicates no breathing
            print(29)  # UseBagValveMask
            continue
        else:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

    # Circulation check
    if not circulation_checked:
        if events[17] > 0.1 and events[16] > 0.1:  # RadialPulsePalpable check
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    # Disability check
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Exposure check
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Handle sats if the probe hasn't been used yet or sats are low
    if not satsProbeUsed or (measured_times[5] > 0 and measured_values[5] < 88):
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # Fluids for circulation support
    if not fluidsGiven and (measured_times[4] < 0.6 or measured_values[4] < 60):
        if not fluidsGiven:
            print(14)  # UseVenflonIVCatheter
            print(15)  # GiveFluids
            fluidsGiven = True
            continue

    # Regularly monitor vital signs if all immediate checks are completed
    if satsProbeUsed and circulation_checked:
        print(16)  # ViewMonitor
        continue

    # End the game if stabilization criteria are met
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    # Default action should not be reached, but in case
    print(0)  # DoNothing
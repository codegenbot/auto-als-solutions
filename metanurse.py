airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_assessed = False

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

    # Airway assessment and interventions
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing assessment and interventions
    if not breathing_assessed:
        if events[7] > 0.5:  # BreathingNone has high relevance
            print(29)  # UseBagValveMask
            continue
        if measured_times[5] == 0:
            print(25)  # UseSatsProbe
            continue
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if measured_times[6] == 0 or measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue
        breathing_assessed = True

    # Circulation assessment
    if not circulation_checked:
        if measured_times[4] == 0:
            print(27)  # UseBloodPressureCuff
            continue
        if measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        circulation_checked = True

    # Disability assessment
    if not disability_checked:
        if events[21] > 0 or events[22] > 0 or events[23] > 0:  # AVPU levels
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    # Exposure assessment
    if not exposure_assessed:
        print(7)  # ExamineExposure
        exposure_assessed = True
        continue

    # Stabilization check
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_assessed
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    # Regular monitoring if no critical condition to address
    print(16)  # ViewMonitor
airway_clear_confirmed = False
circulation_confirmed = False
breathing_confirmed = False
disability_checked = False
exposure_checked = False
critical_condition_handled = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if not critical_condition_handled and (
        (measured_times[5] > 0 and measured_values[5] < 65)
        or (measured_times[4] > 0 and measured_values[4] < 20)
    ):
        print(17)  # StartChestCompression
        critical_condition_handled = True
        continue

    # Check pulse and breathing for critical conditions
    if not airway_clear_confirmed or not breathing_confirmed:
        if events[7] > 0.1:  # BreathingNone
            print(29)  # UseBagValveMask
            continue
        elif events[18] > 0.1:  # RadialPulseNonPalpable
            print(17)  # StartChestCompression
            continue

    # Airway assessment
    if not airway_clear_confirmed:
        if events[3] > 0.1:  # AirwayClear
            airway_clear_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # If there’s an airway problem after confirming it’s clear
    if airway_clear_confirmed and any([events[i] > 0.1 for i in [1, 2, 4, 5, 6]]):
        print(35)  # PerformAirwayManoeuvres
        airway_clear_confirmed = False  # Redo airway check required
        continue

    # Breathing interventions
    if events[7] > 0.1:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    elif measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    elif measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Once breathing is under control
    if not breathing_confirmed and measured_times[5] > 0 and measured_values[5] >= 88:
        breathing_confirmed = True

    # Circulation assessment
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    elif events[18] > 0.1:  # Check circulation again if pulse not palpable
        print(17)  # StartChestCompression
        continue

    # Once circulation is confirmed
    if not circulation_confirmed and measured_times[4] > 0 and measured_values[4] >= 60:
        circulation_confirmed = True

    # Disability assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Exposure check
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Stabilization check
    if (
        airway_clear_confirmed
        and breathing_confirmed
        and circulation_confirmed
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor
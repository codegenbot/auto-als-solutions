airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
oxygen_device_used = False
circulation_interventions_applied = False

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

    # Airway management
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        elif events[4] > 0.1:  # AirwayVomit
            print(31)  # UseYankeurSuctionCatheter
            continue
        elif events[5] > 0.1:  # AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue
        elif events[6] > 0.1:  # AirwayTongue
            print(32)  # UseGuedelAirway
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing assessment and support
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        if not oxygen_device_used:
            print(30)  # UseNonRebreatherMask
            oxygen_device_used = True
            continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation assessment and intervention
    if measured_times[0] > 0 and measured_values[0] < 60:
        if not circulation_interventions_applied:
            print(15)  # GiveFluids
            circulation_interventions_applied = True
            continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Disability assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Monitoring - use wisely
    if not measured_times[4] > 0:  # MAP not recently measured
        print(27)  # UseBloodPressureCuff
        continue
    if not measured_times[5] > 0:  # Sats not recently measured
        print(25)  # UseSatsProbe
        continue

    # Stabilization check
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88  # Sufficient Oxygen Saturation
        and measured_times[6] > 0
        and measured_values[6] >= 8  # Adequate Respiratory Rate
        and measured_times[4] > 0
        and measured_values[4] >= 60  # Adequate MAP
    ):
        print(48)  # Finish
        break

    # If nothing critical, continue monitoring
    print(16)  # ViewMonitor
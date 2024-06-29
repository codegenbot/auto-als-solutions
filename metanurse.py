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
            airway_confired = True
        if events[4] > 0.2 or events[5] > 0.2:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue
        if events[6] > 0.2:  # AirwayTongue, use manoeuvre
            print(36)  # PerformHeadTiltChinLift
            continue
        print(3)  # ExamineAirway
        continue

    # Breathing assessment and interventions
    if not breathing_assessed or events[7] > 0.5:  # BreathingNone
        breathing_assessed = True
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:  # Low sats
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:  # Low respiratory rate
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation assessment
    if measured_times[4] > 0 and measured_values[4] < 60:  # Low MAP
        print(15)  # GiveFluids
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
        and measured_times[5] > 0
        and measured_values[5] >= 88  # Sats at least 88
        and measured_times[6] > 0
        and measured_values[6] >= 8  # Resp Rate at least 8
        and measured_times[4] > 0
        and measured_values[4] >= 60  # MAP at least 60
    ):
        # All conditions for stabilization met
        print(48)  # Finish
        break

    # Regular monitoring if no critical condition to address
    print(16)  # ViewMonitor
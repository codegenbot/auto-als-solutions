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

    # Airway assessment and interventions
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        elif (
            events[4] > 0 or events[5] > 0 or events[6] > 0
        ):  # AirwayVomit/Blood/Tongue
            print(31)  # UseYankeurSuctionCatheter
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing assessment and interventions
    if not breathing_assessed:
        if events[7] > 0.5:  # BreathingNone has high relevance
            print(29)  # UseBagValveMask
            continue
        if measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if measured_times[6] > 0 and measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation assessment
    if not circulation_checked:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        if events[18] > 0.5:  # HeartSoundsMuffled
            print(11)  # GiveAmiodarone
            continue
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Disability assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Exposure assessment
    print(7)  # ExamineExposure

    # Stabilization check
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
        else:
            print(25)  # UseSatsProbe
            continue

    # Regular monitoring if no critical condition to address
    print(16)  # ViewMonitor
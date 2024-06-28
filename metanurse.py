airway_clear_confirmed = False
breathing_assessed = False
circulation_assessed = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway assessment and interventions
    if not airway_clear_confirmed:
        if events[3] > 0.5:  # AirwayClear confirmed
            airway_clear_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue
    else:
        if (
            events[1] > 0.5  # ResponseGroan
            or events[2] > 0.5  # ResponseNone
            or events[4] > 0.5  # AirwayVomit
            or events[5] > 0.5  # AirwayBlood
            or events[6] > 0.5  # AirwayTongue
        ):
            print(35)  # PerformAirwayManoeuvres
            continue
        print(3)  # Recheck Airway condition after intervention
        continue

    # Breathing assessment and intervention
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation assessment and intervention
    if not circulation_assessed:
        print(5)  # ExamineCirculation
        circulation_assessed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Disability checks
    if events[21:24] == [0] * 3:
        print(6)  # ExamineDisability
        continue

    # Exposure checks
    if events[26] > 0.5:
        print(7)  # ExamineExposure
        continue

    # Check stabilization
    if (
        airway_clear_confirmed
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor if no immediate action needed
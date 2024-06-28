airway_clear_confirmed = False

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
        print(3)  # ExamineAirway
        continue
    if events[3] > 0.1:  # AirwayClear confirmed
        airway_clear_confirmed = True

    if events[1] > 0.1 or events[2] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:  # Airway problems
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing assessment and intervention
    if events[8:14] == [0] * 6:  # No detailed breathing checks done
        print(4)  # ExamineBreathing
        continue
    if events[7] > 0.1:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation assessment and intervention
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if (events[16] > 0 and events[17] > 0.5) or (events[16] == 0 and events[17] == 0):  # Unclear pulse information
        print(5)  # ExamineCirculation
        continue

    # Disability checks
    if events[21:24] == [0] * 3:  # AVPU not clear
        print(6)  # ExamineDisability
        continue

    # Exposure checks
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Checking stabilization criteria
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

    # Default action if no specific condition is actively detrimental
    print(16)  # ViewMonitor
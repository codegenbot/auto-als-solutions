airway_clear_confirmed = False
step_count = 0

while step_count < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        step_count += 1
        continue

    # Examine airway if not confirmed clear
    if not airway_clear_confirmed:
        if events[3] > 0.5:  # AirwayClear confirmed
            airway_clear_confirmed = True
        else:
            print(3)  # ExamineAirway
            step_count += 1
            continue

    # Manage airway issues
    if airway_clear_confirmed and (
        events[2] > 0.5 or events[5] > 0.5
    ):  # Airway obstructed (blood or tongue)
        print(31)  # UseYankeurSuctionCatheter
        step_count += 1
        continue

    # Respiratory interventions based on O2 saturation and breathing status
    if measured_times[6] > 0 and measured_values[6] < 8:  # Resp rate low
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:  # Sats low
        print(30)  # UseNonRebreatherMask
        step_count += 1
        continue

    if events[7] > 0.5:  # No breathing
        print(17)  # StartChestCompression
        step_count += 1
        continue

    # Check circulation if unclear pulse info
    if (events[16] > 0 and events[17] > 0.5) or (events[16] == 0 and events[17] == 0):
        print(5)  # ExamineCirculation
        step_count += 1
        continue

    # Check unresponsive or other severe states using AVPU scale
    if events[21:24] == [0] * 3:
        print(6)  # ExamineDisability
        step_count += 1
        continue

    # Check exposure-related problems
    if events[26] > 0.5:
        print(7)  # ExamineExposure
        step_count += 1
        continue

    # Ensuring stabilization criteria are met
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

    # Default fallback to keep monitoring vital signs and status
    if all(mt == 0 for mt in measured_times):
        print(25)  # UseSatsProbe
    else:
        print(16)  # ViewMonitor
    step_count += 1
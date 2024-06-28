airway_clear_confirmed = False
oxygen_needed = False
step_count = 0

while step_count < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        step_count += 1
        continue

    if not airway_clear_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_clear_confirmed = True
        else:
            print(3)  # ExamineAirway
            step_count += 1
            continue

    if measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        if not oxygen_needed:
            print(30)  # UseNonRebreatherMask
            oxygen_needed = True
            step_count += 1
            continue
        else:
            print(29)  # UseBagValveMask
            step_count += 1
            continue

    if measured_times[0] > 0 and (measured_values[0] < 60 or measured_values[0] > 100):
        print(15)  # GiveFluids
        step_count += 1
        continue

    if (
        events[1] > 0.5
        or events[2] > 0.5
        or events[4] > 0.5
        or events[5] > 0.5
        or events[6] > 0.5
    ):
        print(35)  # PerformAirwayManoeuvres
        step_count += 1
        continue

    if (
        measured_times[6] > 0
        and measured_values[6] > 20
        and measured_times[1] > 0
        and measured_values[1] > 8
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor
    step_count += 1
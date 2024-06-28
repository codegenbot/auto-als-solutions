while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Monitor critical conditions triggering immediate lifesaving actions
    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression due to critically low sats
            continue
        elif values[5] < 88:
            print(30)  # UseNonRebreatherMask for low but not critical sats
            continue

    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression due to critical low MAP
            continue
        elif values[4] < 60:
            print(15)  # GiveFluids to boost MAP
            continue

    # Check airway clarity and interventions required
    if events[3] + events[4] + events[5] < 0.5:
        print(3)  # ExamineAirway if no recent clear airway event
        continue

    # Manage insufficient breathing
    if events[7] > 0.5 or (times_recent_measure[6] > 0 and values[6] < 8):
        print(29)  # UseBagValveMask for insufficient breathing
        continue

    # Check for stabilization criteria to finish the game
    if (
        times_recent_measure[5] > 0
        and values[5] >= 88
        and times_recent_measure[6] > 0
        and values[6] >= 8
        and times_recent_measure[4] > 0
        and values[4] >= 60
    ):
        print(48)  # Finish if conditions are stable
        break

    # Default action to gather more information or handle other less critical issues
    print(16)  # ViewMonitor to gather more data
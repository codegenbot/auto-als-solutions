while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    measured_recent = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Immediate critical conditions checks and actions
    if measured_recent[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression for severe low sats
            continue
        elif values[5] < 88:
            print(30)  # UseNonRebreatherMask for low sats
            continue

    if measured_recent[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression for critical low MAP
            continue
        elif values[4] < 60:
            print(15)  # GiveFluids for low MAP
            continue

    # Airway management
    if events[3] + events[4] + events[5] < 0.5:
        print(3)  # ExamineAirway if no clear airway event recently
        continue

    # Breathing management
    busy_with_critical_breathing_issue = False
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask if no breathing
        busy_with_critical_breathing_issue = True

    if not busy_with_critical_breathing_issue and (
        measured_recent[6] > 0 and values[6] < 8
    ):
        print(29)  # UseBagValveMask for low breathing rate
        continue

    # Check overall stability - Finish if conditions are met
    if (
        measured_recent[5] > 0
        and values[5] >= 88
        and measured_recent[6] > 0
        and values[6] >= 8
        and measured_recent[4] > 0
        and values[4] >= 60
    ):
        print(48)  # Finish if all conditions are stable
        break

    # Default safe action if none of the conditions met
    print(16)  # ViewMonitor, as nothing critical is deduced
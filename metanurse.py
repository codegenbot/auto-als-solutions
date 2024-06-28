while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Critical conditions first
    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression for severe low sats
            continue
    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression for critical low MAP
            continue

    # Regular stabilization checks
    if times_recent_measure[5] > 0:
        if values[5] < 88:
            print(30)  # UseNonRebreatherMask for low sats
            continue
    if times_recent_measure[4] > 0:
        if values[4] < 60:
            print(15)  # GiveFluids for low MAP
            continue

    # Airway checks
    if events[3] + events[4] + events[5] < 0.5:
        if events[6] <= 0:
            print(36)  # PerformHeadTiltChinLift if no airway event
        else:
            print(3)  # ExamineAirway
        continue

    # Breathing checks
    if events[7] > 0.5 or (times_recent_measure[6] > 0 and values[6] < 8):
        print(29)  # UseBagValveMask if no breathing or low breathing rate
        continue

    # Complete stabilization check
    if (
        times_recent_measure[5] > 0
        and values[5] >= 88
        and times_recent_measure[6] > 0
        and values[6] >= 8
        and times_recent_measure[4] > 0
        and values[4] >= 60
    ):
        print(48)  # Finish if all conditions are stable
        break

    # Default action if none of the above conditions apply
    print(16)  # ViewMonitor, default safe action
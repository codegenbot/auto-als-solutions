while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression for severe low sats
            continue
        elif values[5] < 88:
            print(30)  # UseNonRebreatherMask for low sats
            continue

    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression for critical low MAP
            continue
        elif values[4] < 60:
            print(15)  # GiveFluids for low MAP
            continue

    if (
        events[3] + events[4] + events[5] + events[6] < 0.1
    ):  # Including AirwayTongue check
        print(3)  # ExamineAirway if no clear airway event recently
        continue

    if events[7] > 0.5 or (times_recent_measure[6] > 0 and values[6] < 8):
        print(29)  # UseBagValveMask if no breathing or low breathing rate
        continue

    # Check for Cardiac arrest
    if events[38] > 0.5:  # HeartRhythmVF - Ventricular Fibrillation
        print(28)  # AttachDefibPads
        continue

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

    print(16)  # ViewMonitor, default safe action
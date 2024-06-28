while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Critical immediate actions for life-threatening conditions
    if events[7] > 0 or events[17] > 0:  # BreathingNone or RadialPulseNonPalpable
        print(17)  # StartChestCompression
        print(28)  # AttachDefibPads
        continue

    # Monitor and manage oxygen saturation
    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression
            continue
        elif values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
    else:
        print(25)  # UseSatsProbe
        continue

    # Ventilation support
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Handling cardiac arrest and inadequate circulation
    if events[17] > 0:  # RadialPulseNonPalpable
        print(17)  # StartChestCompression
        print(39)  # TurnOnDefibrillator
        continue

    # Blood pressure monitoring and management
    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression
            continue
        elif values[4] < 60:
            print(15)  # GiveFluids
            continue
    else:
        print(27)  # UseBloodPressureCuff
        continue

    # Check if patient is stabilized
    c1 = times_recent_measure[5] > 0 and values[5] >= 88
    c2 = events[6] > 0 or (times_recent_measure[6] > 0 and values[6] >= 8)
    c3 = times_recent_measure[4] > 0 and values[4] >= 60
    if c1 and c2 and c3:
        print(48)  # Finish
        break

    # Default action to gather more information
    print(16)  # ViewMonitor if nothing critical detected
while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Immediate life-threatening handling
    if events[7] > 0 or events[17] > 0:  # BreathingNone or RadialPulseNonPalpable
        print(17)  # StartChestCompression
        print(28)  # AttachDefibPads
        continue

    # Oxygen saturation actions
    if times_recent_measure[5] == 0:
        print(25)  # UseSatsProbe
        continue
    elif values[5] < 65:
        print(17)  # StartChestCompression
        continue
    elif values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Blood Pressure Monitoring
    if times_recent_measure[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue
    elif values[4] < 20:
        print(17)  # StartChestCompression
        continue
    elif values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Airway Assessment
    if events[3] + events[4] + events[5] + events[6] < 0.5:  # no clear air signals
        print(3)  # ExamineAirway
        continue

    # Breathing Assessment
    if times_recent_measure[6] == 0:
        print(4)  # ExamineBreathing
        continue
    elif values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Check for stabilization
    if times_recent_measure[5] > 0 and values[5] >= 88 and \
       times_recent_measure[6] > 0 and values[6] >= 8 and \
       times_recent_measure[4] > 0 and values[4] >= 60:
        print(48)  # Finish
        break

    # Default action to gather more data
    print(16)  # ViewMonitor
while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Critical immediate actions for life-threatening conditions
    if times_recent_measure[5] > 0 and values[5] < 65:
        print(17)  # StartChestCompression for severe low sats
        continue
    elif times_recent_measure[5] > 0 and values[5] < 88:
        print(30)  # UseNonRebreatherMask for low sats
        continue

    if times_recent_measure[4] > 0 and values[4] < 20:
        print(17)  # StartChestCompression for critical low MAP
        continue
    elif times_recent_measure[4] > 0 and values[4] < 60:
        print(15)  # GiveFluids for low MAP
        continue

    # Airway management
    if not events[2] and (events[3] + events[4] + events[5] < 0.5):
        print(3)  # ExamineAirway if no clear airway event
        continue

    # Breathing and ventilation management
    if events[7] > 0.5 or (times_recent_measure[6] > 0 and values[6] < 8):
        print(29)  # UseBagValveMask for insufficient breathing
        continue

    # Default action to gather more information
    print(16)  # ViewMonitor, default safe action
    if events[17] > 0:  # RadialPulseNonPalpable response
        print(17)  # StartChestCompression
        continue

    # Measurement needs
    if times_recent_measure[5] <= 0:
        print(25)  # UseSatsProbe for sats measurement
        continue
    if times_recent_measure[4] <= 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Final check if all conditions are met
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
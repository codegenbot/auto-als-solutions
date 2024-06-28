while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Critical immediate actions for life-threatening conditions
    if times_recent_measure[5] > 0 and values[5] < 65:
        print(17)  # StartChestCompression for critical low sats
        continue

    if times_recent_measure[4] > 0 and values[4] < 20:
        print(17)  # StartChestCompression for critical low MAP
        continue

    # Ensure airway is clear
    if events[3] > 0.5:
        if times_recent_measure[5] == 0 or values[5] < 88:
            print(30)  # UseNonRebreatherMask for oxygenation
            continue
    elif events[4] > 0.5 or events[5] > 0.5:
        print(31)  # UseYankeurSuctionCatheter if AirwayBlood or Vomit
        continue
    else:
        print(3)  # ExamineAirway if unsure
        continue

    # Managements for breathing
    if events[7] > 0.5:
        print(29)  # UseBagValveMask for insufficient breathing
        continue

    if times_recent_measure[4] > 0:
        if values[4] < 60:
            print(15)  # GiveFluids for low MAP
            continue
    else:
        print(38)  # TakeBloodPressure to check MAP
        continue

    # Check breathing condition
    if events[6] > 0.5:
        print(4)  # ExamineBreathing for no equal chest expansion
        continue

    if times_recent_measure[6] > 0 and values[6] < 8:
        print(29)  # UseBagValveMask if low respiration rate
        continue

    # Check circulation
    if events[17] > 0.5:
        print(5)  # ExamineCirculation if PulseNonPalpable
        continue

    # Examine responsiveness if disability check required
    if events[22] > 0.5 or events[21] > 0.5:
        print(6)  # ExamineDisability in case of altered consciousness
        continue

    # Final stable check to finish
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

    # Default action to gather more information
    print(16)  # ViewMonitor, default safe action
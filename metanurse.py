while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Immediate critical conditions checks and actions
    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression if severe low sats ( < 65%)
            continue
        elif values[5] < 88:
            print(30)  # UseNonRebreatherMask if low sats ( < 88%)
            continue

    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression if critical low MAP ( < 20mmHg)
            continue
        elif values[4] < 60:
            print(15)  # GiveFluids for low MAP ( < 60mmHg)
            continue

    # Airway management (Clear airway check)
    if not events[3]:  # AirwayClear
        print(3)  # ExamineAirway if airway not recently confirmed clear
        continue

    # Breathing management
    if events[7]:  # BreathingNone
        print(29)  # UseBagValveMask if no breathing detected
        continue
    elif times_recent_measure[1] > 0 and values[1] < 8:
        print(29)  # UseBagValveMask for low respiratory rate ( < 8 breaths per minute)
        continue

    # Circulation management
    if times_recent_measure[4] > 0 and values[4] < 60:
        print(15)  # GiveFluids to improve MAP
        continue

    # Check if stable enough to finish
    if (
        events[3] > 0 and  # AirwayClear
        times_recent_measure[5] > 0 and values[5] >= 88 and  # Sats >= 88%
        times_recent_measure[1] > 0 and values[1] >= 8 and  # RespRate >= 8
        times_recent_measure[4] > 0 and values[4] >= 60  # MAP >= 60mmHg
    ):
        print(48)  # Finish if all conditions are stable
        break

    # Default non-critical time-kill action
    print(16)  # ViewMonitor when under uncertainty

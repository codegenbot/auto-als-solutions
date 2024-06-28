airway_clear = False
breathing_checked = False
circulation_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway
    if not airway_clear:
        if events[3] > 0.5:  # AirwayClear is recent and relevant
            airway_clear = True
        else:
            print(3)  # ExamineAirway
            continue
    else:
        if (
            events[1] > 0.5
            or events[2] > 0.5
            or events[4] > 0.5
            or events[5] > 0.5
            or events[6] > 0.5
        ):
            airway_clear = False
            print(35)  # PerformAirwayManoeuvres
            continue

    # Breathing
    if not breathing_checked:
        if events[7] > 0.5:  # BreathingNone
            print(29)  # UseBagValveMask
            continue
        if measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if measured_times[6] > 0 and measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue
        breathing_checked = True

    # Circulation
    if not circulation_checked:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        circulation_checked = True

    # Disability
    if events[21:25] == [0] * 4:  # No AVPU response
        print(6)  # ExamineDisability
        continue

    # Exposure
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Stabilization check
    if airway_clear and breathing_checked and circulation_checked:
        if (
            measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        ):
            print(48)  # Finish
            break

    print(16)  # ViewMonitor
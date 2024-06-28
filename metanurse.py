airway_confirmed = False
breathing_assessed = False
circulation_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway assessment and interventions
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if airway_confirmed and not breathing_assessed:
        if events[7] > 0.5:  # BreathingNone
            print(29)  # UseBagValveMask
            continue
        elif measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        elif measured_times[6] > 0 and measured_values[6] < 8:
            print(29)  # UseBagValveMask
            continue
        else:
            breathing_assessed = True
            print(4)  # ExamineBreathing
            continue

    if airway_confirmed and breathing_assessed and not circulation_checked:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        else:
            circulation_checked = True
            print(5)  # ExamineCirculation
            continue

    # Disability assessment
    if events[21:25] == [0] * 4:  # No AVPU response
        print(6)  # ExamineDisability
        continue

    # Exposure
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Stabilization check
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0  # Sats at least 88
        and measured_values[6] >= 8
        and measured_times[4] > 0  # Resp Rate at least 8
        and measured_values[4] >= 60  # MAP at least 60
    ):
        print(48)  # Finish
        break

    # Regular monitoring if no other actions needed
    print(16)  # ViewMonitor
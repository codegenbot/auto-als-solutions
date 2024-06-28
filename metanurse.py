airway_clear = False
breathing_assessed = False
circulation_assessed = False
disability_assessed = False
exposure_assessed = False
stabilized = False
steps = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))
    steps += 1

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_clear:
        if events[3] > 0.5:
            airway_clear = True
        else:
            print(3)  # ExamineAirway
            continue

    if not breathing_assessed:
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

    if not circulation_assessed:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        else:
            circulation_assessed = True

    if not disability_assessed:
        if sum(events[21:25]) == 0:  # Checking all AVPU codes are zero
            print(6)  # ExamineDisability
            continue
        else:
            disability_assessed = True

    if not exposure_assessed:
        if events[26] > 0.5:  # ExposurePeripherallyShutdown indicator
            print(7)  # ExamineExposure
            continue
        else:
            exposure_assessed = True

    if (
        airway_clear
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0  # Sats at least 88
        and measured_values[6] >= 8
        and measured_times[4] > 0  # Resp Rate at least 8
        and measured_values[4] >= 60  # MAP at least 60
    ):
        stabilized = True

    if stabilized:
        print(48)  # Finish
        break

    if steps >= 350:
        print(48)  # Finish as a technical timeout fallback
        break

    print(16)  # ViewMonitor as a general action if no other action is taken
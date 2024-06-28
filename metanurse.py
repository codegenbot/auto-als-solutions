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

    # Airway assessment check - clear or needs immediate attention
    if (
        events[1] > 0.5  # ResponseGroan
        or events[2] > 0.5  # ResponseNone
        or events[4] > 0.5  # AirwayVomit
        or events[5] > 0.5  # AirwayBlood
        or events[6] > 0.5  # AirwayTongue
    ):
        print(35)  # PerformAirwayManoeuvres
        continue
    else:
        if events[3] < 0.5:  # Airway not recently cleared
            print(3)  # ExamineAirway
            continue

    # Breathing assessment and management
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation check and management
    if (measured_times[0] > 0 and measured_values[0] < 60) or (
        measured_times[4] > 0 and measured_values[4] < 60
    ):
        print(15)  # GiveFluids
        continue

    # Disability check
    if events[21:25] == [0] * 4:  # No AVPU response
        print(6)  # ExamineDisability
        continue

    # Exposure management
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Check if all stabilization conditions are met
    if (
        events[3] > 0.5  # AirwayClear
        and measured_times[5] > 0
        and measured_values[5] >= 88  # Sats at least 88
        and measured_times[6] > 0
        and measured_values[6] >= 8  # Resp Rate at least 8
        and measured_times[4] > 0
        and measured_values[4] >= 60  # MAP at least 60
    ):
        print(48)  # Finish
        break

    # If no specific action required, continue monitoring
    print(16)  # ViewMonitor
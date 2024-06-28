while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical conditions: Cardiac arrest risks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # A - Airway step
    if events[6] < 0.1:  # AirwayTongue not observed significantly
        print(3)  # ExamineAirway
        continue

    # B - Breathing checks
    if not (
        events[12] > 0 or events[10] > 0
    ):  # Equal chest expansion not observed or unverified
        print(4)  # ExamineBreathing
        continue

    # C - Circulation check
    if events[16] < 0.1:  # RadialPulsePalpable not recently observed
        print(5)  # ExamineCirculation
        continue

    # D - Disability check (using AVPU scale: AVPU_A and AVPU_U typically)
    if events[21] < 0.1 and events[22] < 0.1:  # Not responsive to voice or unresponsive
        print(6)  # ExamineDisability
        continue

    # E - Exposure check
    if (
        events[26] < 0.1
    ):  # ExposurePeripherallyShutdown not recently observed, or unsure
        print(7)  # ExamineExposure
        continue

    # Assessing vital signs to decide further steps
    # If oxygen sat is low or breathing rate is low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    elif measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # If MAP is below normal
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check again if all conditions are now stable
    if all(
        [
            events[3] > 0.1,  # AirwayClear observed
            (events[12] > 0.1 or events[10] > 0.1),  # Breathing is adequate
            events[16] > 0.1,  # Pulse palpable
            measured_times[5] > 0 and measured_values[5] >= 88,
            measured_times[4] > 0 and measured_values[4] >= 60,
            measured_times[6] > 0 and measured_values[6] >= 8,
        ]
    ):
        print(48)  # Finish
        break

    # If no urgent conditions, monitor continuously
    print(16)  # ViewMonitor
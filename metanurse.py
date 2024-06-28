while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate check for cardiac arrest conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Step A: Assess Airway
    if (
        events[3] + events[4] + events[5] + events[6] == 0
    ):  # Airway not checked or not clear
        print(3)  # ExamineAirway
        continue

    # Step B: Assess Breathing
    if events[7] > 0:  # BreathingNone observed
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:  # Low oxygen saturation
        print(30)  # UseNonRebreatherMask
        continue

    # Step C: Assess Circulation
    if measured_times[4] > 0 and measured_values[4] < 60:  # Low MAP
        print(15)  # GiveFluids
        continue

    # Step D: Disability (consciousness level)
    if (
        events[21] + events[22] + events[23] > 0
    ):  # AVPU flags indicate abnormal consciousness
        print(6)  # ExamineDisability
        continue

    # Step E: Assess Exposure
    if (
        events[26] > 0 or events[27] > 0
    ):  # Observable symptoms like ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Stable checks
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

    # Default action if no specific condition is matched
    print(16)  # ViewMonitor
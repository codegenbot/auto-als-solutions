while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediately critical conditions for cardiac arrest
    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Step 2 to enhance: initiate actions through ABCDE assessment protocol
    # A - Check Airway
    if events[3] == 0:  # AirwayClear (now checking instead of defaulting to ViewMonitor)
        print(3)  # ExamineAirway
        continue

    # B - Check Breathing (sufficiency and assistance needed)
    if events[7] > 0.5:  # BreathingNone is high relevance
        print(29)  # UseBagValveMask
        continue

    # Immediate oxygen mask need if sats low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # C - Circulation check (Circulatory support: fluid if low MAP)
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # D - Check Disability: Consciousness
    if events[21] > 0.5 or events[22] > 0.5:  # Unresonable states (AVPU_U or AVPU_V)
        print(6)  # ExamineDisability
        continue

    # E - Exposure check
    if events[26] > 0.5:  # ExposurePeripherallyShutdown is relevant
        print(7)  # ExamineExposure
        continue

    # Scenario complete check and finish
    if measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and measured_values[6] >= 8 and measured_times[4] > 0 and measured_values[4] >= 60:
        print(48)  # Finish
        break

    # If none of the critical condition action was taken, prioritize breathing examining
    if events[4] == 0:  # Breathening check not performed (BreathingSeeSaw etc.)
        print(4)  # ExamineBreathing
        continue

    # If not critical and not first check for airways and breathing, check circulation
    if measured_times[4] == 0:  # MAP checking not done
        print(5)  # ExamineCirculation
        continue

    # Otherwise continue monitoring
    print(16)  # ViewMonitor
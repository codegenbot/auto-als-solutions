while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Emergency conditions triggering immediate actions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Stepwise ABCDE assessment with action plan

    # A - Check airway
    if events[3] <= 0:  # AirwayClear relevance is low or unknown
        print(3)  # ExamineAirway
        continue
    elif (
        events[4] > 0 or events[5] > 0 or events[6] > 0
    ):  # Obstruction due to Vomit, Blood, Tongue
        if events[6] > 0:  # AirwayTongue blockage
            print(37)  # PerformJawThrust
        else:
            print(32)  # UseGuedelAirway
        continue

    # B - Check breathing
    if measured_times[6] == 0 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(4)  # ExamineBreathing
        continue
    elif events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # C - Check circulation
    if measured_times[4] == 0 or (measured_times[4] > 0 and measured_values[4] < 60):
        print(5)  # ExamineCirculation
        continue

    # D - Disability / level of consciousness
    if events[24] <= 0:  # PupilsNormal relevance is low or unknown
        print(6)  # ExamineDisability
        continue

    # E - Check exposure/environment
    print(7)  # ExamineExposure
    continue

    # Checking saturation, respiratory rate, and mean arterial pressure properly
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Providing interventions based on measurements
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check if conditions to finish are met
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

    # Default action if no condition is critical
    print(0)  # DoNothing
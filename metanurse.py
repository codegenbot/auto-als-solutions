while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check if patient requires immediate CPR due to vital signs
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Perform systemic ABCDE checks based on what's most relevant or missing
    if events[3] == 0:  # AirwayClear check not done recently
        print(3)  # ExamineAirway
        continue
    if events[8] == 0:  # BreathingEqualChestExpansion check not done
        print(4)  # ExamineBreathing
        continue
    if events[16] == 0:  # RadialPulsePalpable check not done
        print(5)  # ExamineCirculation
        continue
    if events[21] == 0 or events[22] == 0 or events[23] == 0:  # AVPU checks
        print(6)  # ExamineDisability
        continue
    if events[26] == 0:  # ExposurePeripherallyShutdown not checked
        print(7)  # ExamineExposure
        continue

    # Act on critical observations
    if events[5] > 0.1:  # Airway obstructed by vomit or blood
        print(31)  # UseYankeurSuctionCatheter
        continue
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Manage breathing and oxygenation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Manage circulation
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check for stabilization
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

    print(0)  # DoNothing
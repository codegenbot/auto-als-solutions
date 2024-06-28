while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Start chest compression if critical conditions are met
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Immediate check for airway blockage if not checked or if there's indication of blockage
    if events[3] <= 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
        print(3)  # ExamineAirway
        continue

    # Immediate actions for airway management if no clear breath sounds or effective breathing
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Monitoring setup if not done yet
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Check breathing and circulation
    if events[4] > 0 or events[5] > 0 or events[6] > 0:  # Check complications in airway
        print(3)  # ExamineAirway
        continue
    if (
        events[7] > 0.1 or events[8] > 0.1 or events[9] > 0.1
    ):  # Ineffective breathing patterns
        print(4)  # ExamineBreathing
        continue
    if events[16] == 0:  # RadialPulseNonPalpable
        print(5)  # ExamineCirculation
        continue

    # Provide necessary interventions based on observations
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check if conditions to finish are met
    if (
        events[3] > 0
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Idle action if no critical action is needed
    print(0)  # DoNothing
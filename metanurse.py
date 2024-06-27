while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate actions based on critical airway or breathing conditions
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Immediate threats from vital sign measurements
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Update on Vital Signs if any measurement is not recent or missing
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Act based on low oxygen saturation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Act based on low Respiratory Rate
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Act based on low Mean Arterial Pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Checking for stability to possibly finish the scenario
    if measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and measured_values[6] >= 8 and measured_times[4] > 0 and measured_values[4] >= 60:
        print(48)  # Finish
        break

    # Examine if required information is missing
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue
    if events[7] == 0 and events[8] == 0 and events[9] == 0 and events[10] == 0 and events[11] == 0 and events[12] == 0 and events[13] == 0 and events[14] == 0:
        print(4)  # ExamineBreathing
        continue
    if events[16] == 0 and events[17] == 0:
        print(5)  # ExamineCirculation
        continue
    if events[21] == 0 and events[22] == 0 and events[23] == 0:
        print(6)  # ExamineDisability
        continue
    if events[26] == 0 and events[27] == 0:
        print(7)  # ExamineExposure
        continue

    print(0)  # DoNothing if nothing else is required
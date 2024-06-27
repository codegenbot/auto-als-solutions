while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    if events[7] == 1:  # BreathingNone
        print(17)  # StartChestCompression
        continue

    # Stabilization criteria
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

    # Direct measurements for stabilization
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue

    if measured_times[4] == 0:
        print(38)  # TakeBloodPressure
        continue

    # Airway management
    if events[3:7] == [0, 0, 0, 0]:  # No airway info
        print(3)  # ExamineAirway
        continue

    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(32)  # UseGuedelAirway
        continue

    # Breathing management
    if events[7] == 1 or events[8] > 0 or events[9] > 0:  # Critical breathing issues
        if measured_values[6] < 12:
            print(29)  # UseBagValveMask
        else:
            print(30)  # UseNonRebreatherMask
        continue

    # Circulation management
    if events[17] == 1 or (measured_times[0] > 0 and measured_values[0] > 100):  # RadialPulseNonPalpable, high heart rate
        print(5)  # ExamineCirculation
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing if nothing else is required
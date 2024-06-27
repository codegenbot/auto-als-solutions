while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving measures
    if events[7] > 0:  # BreathingNone
        print(17)  # StartChestCompression
        continue

    if events[17] > 0:  # RadialPulseNonPalpable
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if measured_times[4] > 0 and measured_values[4] < 20:
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

    # Direct measurements
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue

    if measured_times[4] == 0:
        print(38)  # TakeBloodPressure
        continue

    # Airway management
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(32)  # UseGuedelAirway
        continue

    # Breathing assessment and intervention
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if events[8] > 0 or events[9] > 0:  # BreathingSnoring or BreathingSeeSaw
        print(4)  # ExamineBreathing
        continue

    # Circulation assessment and management
    if events[16] == 0 and events[17] > 0:  # RadialPulseNonPalpable
        print(5)  # ExamineCirculation
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Default action
    print(0)  # DoNothing
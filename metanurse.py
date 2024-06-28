while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Assess response and airway immediately
    if not events[0] and not events[1] and events[2]:
        print(3)  # ExamineAirway
        continue

    # Critical conditions first
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Regular checks via examinations
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        if measured_times[5] == 0:
            print(25)  # UseSatsProbe
        elif measured_times[6] == 0:
            print(4)  # ExamineBreathing
        elif measured_times[4] == 0:
            print(38)  # TakeBloodPressure
        continue

    # Intervention based on airway and breathing assessments
    if events[3] > 0 or events[4] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue
    elif events[7]:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    elif events[6]:  # AirwayTongue
        print(32)  # UseGuedelAirway
        continue

    # Circulatory support
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Oxygenation intervention
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check overall condition before finishing
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

    # Default action - if no conditions triggered above
    print(0)  # DoNothing
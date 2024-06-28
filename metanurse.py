while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions requiring resuscitation
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway and ventilation checks
    if events[5]:  # AirwayVomit or Blood observe, need suction
        print(31)  # UseYankeurSuctionCatheter
        continue
    if events[6]:  # AirwayTongue, need airway management
        print(36)  # PerformHeadTiltChinLift
        continue
    if events[7]:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Examine if missing vital signs data
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        if measured_times[5] == 0:
            print(25)  # UseSatsProbe
        elif measured_times[4] == 0:
            print(27)  # UseBloodPressureCuff
        else:
            print(16)  # ViewMonitor
        continue

    # Specific conditions management based on measured values
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Reexamine phases if no specific actions are necessary
    if not any([events[i] >= 0.1 for i in range(33)]):
        print(3)  # ExamineAirway
        continue
    if not any(events[8:15]) or measured_times[6] == 0:
        print(4)  # ExamineBreathing
        continue
    if not any(events[16:19]) or measured_times[4] == 0:
        print(5)  # ExamineCirculation
        continue
    if not any(events[21:25]) or measured_times[3] == 0:
        print(6)  # ExamineDisability
        continue
    if not any(events[26:33]):
        print(7)  # ExamineExposure
        continue

    # Check for stabilization
    if (
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default action if no other action is trigged
    print(0)  # DoNothing
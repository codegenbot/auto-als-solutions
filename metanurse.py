while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate actions based on critical conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Examine Airway and clear if necessary
    if any(o > 0 for o in events[3:7]):  # If any airway obstruction events are relevant
        if events[4] > 0:  # AirwayVomit
            print(31)  # UseYankeurSuctionCatheter
            continue
        elif events[5] > 0:  # AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue
        else:
            print(35)  # PerformAirwayManoeuvres
            continue
    else:
        print(3)  # ExamineAirway
        continue

    # Breathing checks and measures
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    elif measured_times[5] == 0 or measured_values[5] < 88:  # Oxygen saturation check
        print(30)  # UseNonRebreatherMask
        continue
    else:
        print(4)  # ExamineBreathing
        continue

    # Circulation checks and measures
    if measured_times[4] == 0 or measured_values[4] < 60:  # MAP check
        print(15)  # GiveFluids
        continue
    elif any(o == 0 for o in events[16:18]):  # If pulse not measurable or not palbable
        print(5)  # ExamineCirculation
        continue
    else:
        print(38)  # TakeBloodPressure
        continue

    # Disability checks
    if events[21] == 0 and events[22] == 0 and events[23] == 0:
        print(6)  # ExamineDisability
        continue

    # Exposure checks
    if events[26] == 0 and events[27] == 0:
        print(7)  # ExamineExposure
        continue

    # Check for stabilized condition
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

    # Default action
    print(0)  # DoNothing
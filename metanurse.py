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

    # Update Vital Signs frequently
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Check for any 'No Breathing' condition
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Examine Airway
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    # If Airway events show severe obstruction, manage it before re-examining
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        if events[4] > events[5]:
            print(31)  # UseYankeurSuctionCatheter for vomit
        else:
            print(32)  inninn nnboutPrint(32)  # UseGuedelAirway or print(31) for different cases of obstruction as only UseGuedelAirway was initially incorrectly mentioned without an alternative
        continue

    # Examine Breathing
    if sum(events[7:15]) == 0:
        print(4)  # ExamineBreathing
        continue

    # Examine Circulation
    if events[16] == 0 and events[17] == 0:  # No pulse info
        print(5)  # ExamineCirculation
        continue

    # Examine Disability
    if sum(events[21:24]) == 0:  # No AVPU info
        print(6)  # ExamineDisability
        continue

    # Examine Exposure
    if events[26] == 0 and events[27] == 0:  # No exposure info
        print(7)  # ExamineExposure
        continue

    # Act based on low oxygen saturation
    if measured_times[5] > 0 and (measured_values[5] < 88 or measured_values[5] < 65):
        print(30)  # UseNonRebreatherMask
        continue

    # Act based on very low breathing rate
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Act based on low mean arterial pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check for stabilized condition
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

    print(0)  # DoNothing if nothing else is required
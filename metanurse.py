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

    # No breathing action detected
    if events[7] > 0:  # BreathingNone
        print(
            29
        )  # UseBagValadigmExamining Airway and its complications based on events
    if events[4] > 0:  # AirwayVomit
        print(32)  # UseGuedelAirway
        continue
    if events[5] > 0:  # AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Airway check if no recent details
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    # Oxygen saturation management
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Respiratory rate management
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulatory pressure management
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Ensuring examinations happen if nothing else is urgent
    if all(e == 0 for e in events[7:15]):  # All breathing check events
        print(4)  # ExamineBreathing
        continue

    if (
        measured_times[0] == 0 or measured_times[1] == 0 or measured_times[2] == 0
    ):  # If pulse, HR, BP unseen
        print(5)  # ExamineCirculation
        continue

    print(0)  # DoNothing if nothing else is required
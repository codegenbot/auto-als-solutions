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

    # Stabilize and monitor critical measurements
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Immediate intervention if John stops breathing
    if events[7] > 0:  # BreathingNone
        print(17)  # StartChestCompression
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

    # Examine crucial components if not yet evaluated or in case of significant events
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(
            32 if events[4] > 0 else 31
        )  # UseGuedelAirway or UseYankeurSuctionCatheter
        continue

    if all(x == 0 for x in events[10:15]):  # No recent breathing information
        print(4)  # ExamineBreathing
        continue

    if events[16] == 0 and events[17] == 0:  # No pulse info
        print(5)  # ExamineCirculation
        continue

    if events[21] == 0 and events[22] == 0 and not (events[23] > 0 or events[24] > 0):
        print(6)  # ExamineDisability
        continue

    if events[26] == 0 and events[27] == 0:  # No exposure info
        print(7)  # ExamineExposure
        continue

    # Responsive treatments based on real-time measurements
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing if no other immediate action is required
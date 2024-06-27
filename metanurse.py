while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions
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

    # Emergency non-breathing
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Stabilized condition check
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

    # Airway examinations
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter or appropriate response
        continue

    # Breath check and related actions
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation and pressure handling
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing if no other immediate action is needed
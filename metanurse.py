while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check critical conditions leading to cardiac arrest
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway check
    if events[2] > 0:  # ResponseNone
        print(3)  # ExamineAirway
        continue

    # Clear airway if obstructed
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Breathing assessment if not breathing
    if events[7] > 0:  # BreathingNone
        if measured_times[1] == 0:  # No recent respiratory rate measurement
            print(25)  # UseSatsProbe
            continue
        print(4)  # ExamineBreathing
        continue

    # Fluids for circulation issues
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # View monitor for updated status
    if measured_times[4] == 0 or measured_times[5] == 0 or measured_times[6] == 0:
        print(16)  # ViewMonitor
        continue

    # Oxygen if sats low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # End if stabilized
    if all(
        [
            measured_times[5] > 0 and measured_values[5] >= 88,
            measured_times[6] > 0 and measured_values[6] >= 8,
            measured_times[4] > 0 and measured_values[4] >= 60,
        ]
    ):
        print(48)  # Finish
        break

    # Default action
    print(0)  # DoNothing
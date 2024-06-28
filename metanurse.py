while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical conditions that require immediate response
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway assessment and management
    if events[3] == 0:  # AirwayClear not triggered
        print(3)  # ExamineAirway
        continue
    if events[5] > 0.5 or events[6] > 0.5:  # Airway obstruction evident (Vomit, Blood)
        print(31)  # UseYankeurSuctionCatheter or appropriate intervention
        continue

    # Breathing assessment and management
    if (
        measured_times[5] == 0 or measured_values[5] < 88
    ):  # No recent sats or sats are low
        if events[7] > 0.5:  # BreathingNone
            print(29)  # UseBagValveMask
        else:
            print(24)  # UseMonitorPads (to facilitate pulse oximetry)
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation assessment and management
    if measured_times[4] > 0:
        if measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        elif measured_values[4] >= 60:
            print(
                5
            )  # ExamineCirculation if more data needed or maintenance of monitoring
        else:
            print(38)  # TakeBloodPressure
    else:
        print(27)  # UseBloodPressureCuff to get new MAP reading
        continue

    # Check if patient is stabilised
    if (
        events[3] > 0.5  # Airway clear
        and measured_times[5] > 0
        and measured_values[5] >= 88  # Sats OK
        and measured_times[6] > 0
        and measured_values[6] >= 8  # Respiratory rate OK
        and measured_times[4] > 0
        and measured_values[4] >= 60  # MAP OK
    ):
        print(48)  # Finish
        break

    # Default action if no other immediate actions required
    print(0)  # DoNothing
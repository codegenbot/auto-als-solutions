airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        if measured_values[5] < 65:
            print(28)  # AttachDefibPads if sats too low
        if measured_values[4] < 20:
            print(17)  # StartChestCompression if MAP too low
        continue

    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_confirmed = True
        else:
            print(
                31
            )  # UseYankeurSuctionCatheter or choose appropriate action to clear airway
            continue

    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if not circulation_checked:
        if measured_times[4] > 0:
            if measured_values[4] < 60:
                print(15)  # GiveFluids
            else:
                circulation_checked = True
        else:
            print(27)  # UseBloodPressureCuff
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    if (
        airway_confirmed
        and circulation_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
    ):
        print(48)  # Finish
        break
    print(16)  # ViewMonitor as a fallback to refresh data and continue assessment
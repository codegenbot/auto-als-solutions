while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examine Airway once and only if unclear status
    if max(events[3:7]) < 0.1:  # vague presence of airway clarity
        print(3)  # ExamineAirway
        continue

    # Respond to NoBreathing quickly
    if events[7] > 0.5 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Ensure adequate oxygen saturation
    if measured_times[5] > 0:
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
        else:
            # Check Circulation
            if measured_times[4] > 0 and measured_values[4] < 60:
                print(15)  # GiveFluids
            else:
                # At this point, perform regular checks or prepare to end simulation
                # As stability is established when conditions are met
                if measured_times[4] > 0 and measured_values[4] >= 60:
                    print(48)  # Finish
                    break
                else:
                    print(
                        28
                    )  # AttachDefibPads for ECG monitoring and possible defib if rhythms off
    else:
        print(25)  # UseSatsProbe to get accurate oxygen saturation
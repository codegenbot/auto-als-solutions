while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical condition immediate response
    if measured_times[4] > 0 and measured_values[4] < 20:  # mean arterial pressure
        print(17)  # StartChestCompression
        continue
    if measured_times[5] > 0 and measured_values[5] < 65:  # oxygen saturation
        print(17)  # StartChestCompression
        continue

    # Checking the airway
    if events[3] + events[4] + events[5] < 0.5:  # No clear airway sign
        print(3)  # ExamineAirway
        continue

    # Treat breathing problems
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:  # oxygen saturation
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation problems
    if measured_times[4] > 0 and measured_values[4] < 60:  # mean arterial pressure
        print(15)  # GiveFluids
        continue

    # Checking for completion of scenario
    if (
        events[3] > 0.5
        and measured_values[5] >= 88
        and measured_values[6] >= 8
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # View monitor for recent measurements for vitals
    if any(
        mt == 0 for mt in measured_times[:3]
    ):  # heart rate, resp rate, capillary glucose
        print(16)  # ViewMonitor
        continue

    # Default action if nothing urgent or specific required
    print(0)  # DoNothing
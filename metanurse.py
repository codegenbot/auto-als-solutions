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

    # No recent sats or blood pressure: attach and monitor
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] == 0:
        print(16)  # ViewMonitor
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # ABCDE Process
    if events[3] <= 0.5:  # AirwayClear is not clear
        print(3)  # ExamineAirway
        continue
    if any(events[10:14]):  # Check for breathing issues
        print(4)  # ExamineBreathing
        continue
    if (
        events[5] > 0.5 or events[18] <= 0.5
    ):  # RadialPulseNonPalpable or HeartSoundsMuffled
        print(5)  # ExamineCirculation
        continue
    if events[22] <= 0.5 and events[23] <= 0.5:  # Check for consciousness
        print(6)  # ExamineDisability
        continue
    if events[26] > 0.5 or events[27] > 0.5:  # Exposure indicators
        print(7)  # ExamineExposure
        continue

    # Recheck crucial measurements if uncertain conditions
    if measured_times[4] > 0 and measured_times[5] > 0 and measured_times[6] > 0:
        if not (
            measured_values[5] >= 88
            and measured_values[6] >= 8
            and measured_values[4] >= 60
        ):
            print(16)  # ViewMonitor
            continue

    # Finish if conditions are satisfied
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

    # Default is to review monitor or routines
    print(16)  # ViewMonitor
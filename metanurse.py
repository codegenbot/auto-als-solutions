while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handle life-threatening situations first
    if events[7] > 0.5 or (measured_times[6] > 0 and measured_values[6] < 8):  # BreathingNone or low respiration rate
        print(29)  # UseBagValveMask
        continue
    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Airway decision making
    if events[3] < 0.5:  # AirwayClear not recently confirmed
        print(3)  # ExamineAirway
        continue
    
    if measured_times[4] > 0 and measured_values[4] < 60:  # Low MAP indicates potential circulation issue
        print(15)  # GiveFluids
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:  # Low oxygen saturation
        print(30)  # UseNonRebreatherMask
        continue
    
    # Check response and disability
    if events[22:26] == [0] * 4:  # No clear response recorded
        print(8)  # ExamineResponse
        continue
    if events[24] < 0.5 and events[25] < 0.5:  # No pupil check done recently or abnormal
        print(6)  # ExamineDisability
        continue

    # Exposure and general checks
    if events[26] > 0.5:  # Severe peripheral shutdown indicates critical exposure issues
        print(7)  # ExamineExposure
        continue

    # Stabilization check
    if (
        events[3] > 0.5 and  # AirwayClear
        measured_times[5] > 0 and measured_values[5] >= 88 and  # Sats at least 88
        measured_times[6] > 0 and measured_values[6] >= 8 and  # Resp Rate at least 8
        measured_times[4] > 0 and measured_values[4] >= 60  # MAP at least 60
    ):
        print(48)  # Finish
        break

    # Default action if no critical issues
    print(16)  # ViewMonitor
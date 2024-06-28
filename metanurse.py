while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical issues
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway checks: assuming event indices follow the listed names and documentation
    if events[3] < 0.5 and any(events[i] > 0.5 for i in [4, 5, 6]):  # Any airway occlusion by blood, vomit, etc
        print(31)  # UseYankeurSuctionCatheter
        continue
    elif events[3] < 0.5:  # No clear airway signs 
        print(3)  # ExamineAirway
        continue

    # Breathing issues
    if events[7] > 0.5:
        print(29)  # UseBagValveMask
    elif measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValveMask
        continue
    elif measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask      
        continue

    # Circulation issues
    if measured_times[0] > 0 and measured_values[0] < 60:
        print(15)  # GiveFluids
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check if all stabilisation conditions are met
    if all([
        measured_times[5] > 0 and measured_values[5] >= 88,
        measured_times[1] > 0 and measured_values[1] >= 8,
        measured_times[4] > 0 and measured_values[4] >= 60
    ]):
        print(48)  # Finish
        break

    # Regular checking actions
    print(16)  # ViewMonitor
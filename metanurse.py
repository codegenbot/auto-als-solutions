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

    # Airway assessment and management
    if events[3] < 0.5:
        print(3)  # ExamineAirway
        continue
    if any(events[i] > 0.5 for i in [4, 5, 6]):  # Obstruction by blood, vomit, or tongue
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Breathing assessment and management
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation checks and management
    if measured_times[0] > 0 and measured_values[0] < 60:
        print(15)  # GiveFluids
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
        
    # Disability - Check consciousness
    if events[21] > 0.5 or events[22] > 0.5:  # AVPU_U or AVPU_V
        print(6)  # ExamineDisability
        continue
     
    # If patient is stable based on basic conditions
    if (measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[1] > 0 and measured_values[1] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor  # Default action to gather more data
while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate actions based on critical conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Gather comprehensive monitoring
    if any(t == 0 for t in measured_times):
        print(16)  # ViewMonitor
        continue

    # Handle No Breathing or inadequate ventilation
    if events[7]:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Emergency response to airway blockage
    if events[4] > 0 or events[5] > 0: # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSucionCatheter
        continue

    # Examine each aspect that is not confirmed
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    if sum(events[7:15]) == 0:
        print(4)  # ExamineBreathing
        continue

    if events[16] == 0 and events[17] == 0:  # RadialPulsePalpable and RadialPulseNonPalpable
        print(5)  # ExamineCirculation
        continue

    if sum(events[21:24]) == 0:  # AVPU info
        print(6)  # ExamineDisability
        continue

    if events[26] == 0 and events[27] == 0:  # Exposure info
        print(7)  # ExamineExposure
        continue

    # Interventions based on status
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check for stabilized condition
    stabilized = all([
        measured_times[5] > 0 and measured_values[5] >= 88,
        measured_times[6] > 0 and measured_values[6] >= 8,
        measured_times[4] > 0 and measured_values[4] >= 60
    ])
    if stabilized:
        print(48)  # Finish
        break

    print(0)  # DoNothing if nothing else is required
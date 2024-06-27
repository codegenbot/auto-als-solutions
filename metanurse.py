while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate actions based on critical conditions (prioritize checking)
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Update Vital Signs frequently monitor and breathing
    if any(measurement == 0 for measurement in measured_times[:3]) or measured_times[5] == 0 or measured_times[6] == 0:  # Vital signs measurements
        print(16)  # ViewMonitor
        continue

    # No breathing - immediate action required
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Check Airway obstructions and manage if found
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Periodical checks for ABCDEs if no recent events or measurements
    if all(events[:3] == 0):  # Airway Issues
        print(3)  # ExamineAirway
        continue
    if all(events[8:15] == 0):  # Breathing Issues
        print(4)  # ExamineBreathing
        continue
    if events[16] == 0 and events[17] == 0:  # Circulation - Pulse
        print(5)  # ExamineCirculation
        continue
    if all(events[21:24] == 0):  # Disability - Consciousness
        print(6)  # ExamineDisability
        continue
    if all(events[26:28] == 0):  # Exposure
        print(7)  # ExamineExposure
        continue

    # Act based on low oxygen saturation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Act based on low respiratory rate
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Act based on low mean arterial pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check for stabilized condition
    if (
        events[3] > 0  # AirwayClear
        and measured_times[5] > 0 and measured_values[5] >= 88
        and measured_times[6] > 0 and measured_values[6] >= 8
        and measured_times[4] > 0 and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break
    
    print(0)  # DoNothing if nothing else is required
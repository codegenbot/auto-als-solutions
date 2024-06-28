while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check for critical conditions that require immediate response
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Check if the airway is examined and clear
    if events[3] == 0:  # AirwayClear not triggered
        print(3)  # ExamineAirway
        continue

    # If no breathing, intervene with emergency breathing support
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # If breathing is severely compromised, support immediately
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Ensure vital stats are monitored if measurement times are zero
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Oxygen support if saturation is low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Fluids if mean arterial pressure is low
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Ending the loop if stabilization conditions are met
    if (
        events[3] > 0  # Airway clear
        and measured_times[5] > 0 and measured_values[5] >= 88  # Sats stabilized
        and measured_times[6] > 0 and measured_values[6] >= 8  # Resps adequate
        and measured_times[4] > 0 and measured_values[4] >= 60  # MAP adequate
    ):
        print(48)  # Finish
        break
    
    # Default action if no critical interventions needed immediately
    print(0)  # DoNothing
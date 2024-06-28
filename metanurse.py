while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate checks for critical conditions
    critical_airway_blocked = (
        events[4] > 0.5 or events[5] > 0.5
    )  
    critical_no_breathing = events[7] > 0.5  
    critical_low_sats = measured_times[5] > 0 and measured_values[5] < 65
    critical_low_map = measured_times[4] > 0 and measured_values[4] < 20

    if critical_low_sats or critical_low_map:
        print(17)  
        continue

    # Check Airway
    if (
        events[3] < 0.5 and events[4] < 0.5 and events[5] < 0.5 and events[6] < 0.5
    ) or critical_airway_blocked:
        print(3)  
        continue

    # Check Breathing
    if critical_no_breathing:
        print(29)  
        continue

    # Check oxygen saturation and respiratory rate
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  
        continue

    # Check Circulation
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  
        continue

    # If there are enough observations to conclude the patient is stabilized, finish the scenario
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  
        break

    # Default action to gather more information
    print(16)  
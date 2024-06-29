observations = input().split()
events = list(map(float, observations[:39]))
measured_times = list(map(float, observations[39:46]))
measured_values = list(map(float, observations[46:]))

# Essential Variables
has_clear_airway = events[3] > 0.5  # AirwayClear flag
is_breathing_critical = measured_times[6] > 0 and measured_values[6] < 8
is_sats_critical = measured_times[5] > 0 and measured_values[5] < 65
is_map_critical = measured_times[4] > 0 and measured_values[4] < 20

# Critical Conditions Handling
if is_sats_critical or is_map_critical:
    print(17)  # Start Chest Compression if in critical condition
elif is_breathing_critical:
    print(29)  # Use Bag Valve Mask if breathing is critically low

# Stabilization Processes
elif not has_clear_airway:
    print(3)  # Examine Airway if not cleared
elif measured_times[5] == 0 or measured_values[5] < 88:  # Checking Oxygen Saturation
    print(25)  # Use Sats Probe if O2 sat < 88%
elif measured_times[4] == 0 or measured_values[4] < 60:  # Checking MAP
    print(27)  # Use Blood Pressure Cuff if MAP < 60mmHg
elif measured_times[6] > 0 and measured_values[6] < 12:
    print(28)  # Use Non-Rebreather Mask to stabilize breathing

# Normal Operation Monitoring
else:
    print(48)  # Finish if all conditions are stable
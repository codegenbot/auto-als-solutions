airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # Start Chest Compression
        continue

    if not airway_confirmed and events[3] < 0.1:
        print(3)  # Examine Airway
        continue

    airway_confirmed = True

    if not breathing_assessed and events[9] < 0.7:
        print(4)  # Examine Breathing
        continue

    breathing_assessed = True

    if not circulation_checked and (events[16] < 0.1 and events[17] < 0.1):
        print(5)  # Examine Circulation
        continue

    circulation_checked = True

    if not disability_checked and events[22] < 0.1:
        print(6)  # Examine Disability
        continue

    disability_checked = True

    if not exposure_checked:
        print(7)  # Examine Exposure
        exposure_checked = True
        continue

    initial_assessments_done = True

    if initial_assessments_done and (measured_times[5] == 0 or measured_values[5] < 88):
        if not satsProbeUsed:
            print(25)  # Use Sats Probe
            satsProbeUsed = True
            continue
        else:
            print(16)  # View Monitor
            continue
  
    if (measured_times[4] == 0 or measured_values[4] < 60):
        print(14)  # Use Venflon IVCatheter
        continue

    if (measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    # If none of the above conditions are met, do nothing to observe further changes
    print(0)  # Do Nothing
airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_examined = False
monitor_pads_used = False
sats_probe_used = False
bp_cuff_used = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)
        continue

    if not airway_confirmed:
        if events[3] > 0.5:
            airway_confirmed = True
        elif any(events[i] > 0 for i in [4, 5, 6]):
            print(31)
            continue
        else:
            print(3)
            continue

    if events[7] > 0.5:
        print(29)
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        if not sats_probe_used:
            print(25)
            sats_probe_used = True
            continue
        print(30)  # Non-rebreather mask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # Bag Valve Mask
        continue

    if not breathing_assessed:
        print(4)
        breathing_assessed = True
        continue

    if events[18] > 0 or events[21] > 0 or events[23] > 0:
        print(11)  # Amiodarone if heart complications
        continue

    if measured_times[0] > 0 and measured_values[0] < 60:
        print(14)  # Venflon IVCatheter if heart rate low
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        if not bp_cuff_used:
            print(27)  # Blood pressure cuff
            bp_cuff_used = True
            continue
        print(15)  # Give fluids
        continue
    
    if not circulation_checked:
        print(5)
        circulation_checked = True
        continue

    if not disability_checked:
        print(6)
        disability_checked = True
        continue

    if not exposure_examined:
        print(7)
        exposure_examined = True
        continue

    if all([
        airway_confirmed, breathing_assessed, circulation_checked, disability_checked, exposure_examined,
        measured_times[5] > 0, measured_values[5] >= 88,
        measured_times[6] > 0, measured_values[6] >= 8,
        measured_times[4] > 0, measured_values[4] >= 60
    ]):
        print(48)
        break

    print(16)  # View monitor if no immediate actions required
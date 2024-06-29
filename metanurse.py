airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_examined = False
crucial_intervention_done = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # Start chest compression
        crucial_intervention_done = True
        continue

    if not airway_confirmed:
        if events[3] > 0:
            airway_confirmed = True
        elif any(
            events[i] > 0 for i in [4, 5, 6]
        ):  # Vomit, blood, or tongue obstructing airway
            print(31)  # Use Yankeur suction catheter
            continue
        else:
            print(3)  # Examine Airway
            continue

    if crucial_intervention_done:
        if events[7] > 0:  # BreathingNone
            print(29)  # Use Bag Valve Mask
            continue
        if measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # Use NonRebreatherMask
            continue
        if measured_times[6] > 0 and measured_values[6] < 8:
            print(29)  # Use Bag Valve Mask
            continue

    if not breathing_assessed:
        print(4)  # Examine Breathing
        breathing_assessed = True
        continue

    if events[17] > 0.5:  # RadialPulseNonPalpable
        print(10)  # Give Adrenaline
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # Give Fluids
        continue
    if not circulation_checked:
        print(5)  # Examine Circulation
        circulation_checked = True
        continue

    if not disability_checked:
        print(6)  # Examine Disability
        disability_checked = True
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and not exposure_examined
    ):
        print(7)  # Examine Exposure
        exposure_examined = True
        continue

    if all(
        [
            airway_confirmed,
            breathing_assessed,
            circulation_checked,
            disability_checked,
            exposure_examined,
            measured_times[5] > 0,
            measured_values[5] >= 88,
            measured_times[6] > 0,
            measured_values[6] >= 8,
            measured_times[4] > 0,
            measured_values[4] >= 60,
        ]
    ):
        print(48)  # Finish
        break

    print(16)  # View Monitor (default action when unsure)
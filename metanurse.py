airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check critical conditions first
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check Airway
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    elif events[3] > 0.5:  # AirwayClear event is recent and significant
        airway_confirmed = True

    # Check Breathing
    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        continue
    elif airway_confirmed and events[10] > 0.5:  # BreathingEqualChestExpansion is recent and significant
        breathing_assessed = True

    # Check Circulation
    if breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        continue
    elif breathing_assessed and events[16] > 0.5:  # RadialPulsePalpable is recent and significant
        circulation_checked = True

    # Check Disability
    if circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        continue
    elif circulation_checked and (events[24] > 0.5 or events[23] > 0.5):  # PupilsNormal or PupilsPinpoint are significant
        disability_checked = True

    # Check if all assessments done and stabilize patient
    if all([airway_confirmed, breathing_assessed, circulation_checked, disability_checked]):
        if (measured_times[4] > 0 and measured_values[4] >= 60) \
           and (measured_times[5] > 0 and measureds_values[5] >= 88) \
           and (measured_times[6] > 0 and measured_values[6] >= 8):

            print(48)  # Finish
            break
        else:
            if measured_times[5] <= 0:
                print(25)  # Use Sats Probe
                continue
            elif measured_times[4] <= 0:
                print(27)  # Use Blood Pressure Cuff
                continue

    # Monitoring critical patient conditions in loop
    if (measured_times[1] > 0 and measured_values[1] < 8) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(22)  # Bag During CPR
        continue
    elif measured_times[5] <= 0:
        print(25)  # Use Sats Probe
        continue
    elif measured_times[4] <= 0:
        print(27)  # Use Blood Pressure Cuff
        continue

    # Default monitoring action
    print(16)  # ViewMonitor
    continue
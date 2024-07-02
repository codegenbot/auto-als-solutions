airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate action for life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check airway
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    elif events[3] > 0:
        airway_confirmed = True

    # Check breathing
    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Check circulation
    if breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Check disability
    if circulation_checked and not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Check exposure
    if disability_checked and not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        initial_assessments_done = True
        continue

    # Use Sats Probe after initial assessments
    if initial_assessments_done and not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # Non-rebreather mask if sats are low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Blood Pressure Cuff
    if initial_assessments_done and not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    # Fluids if mean arterial pressure is low
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check finish conditions
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default action if no other conditions met
    print(0)  # DoNothing
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

    # Immediate critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # First, ensure airway is checked
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
            airway_confirmed = True
        continue

    # Next check breathing
    if not breathing_assessed and airway_confirmed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Check circulation
    if not circulation_checked and breathing_assessed:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Use SATs probe early if not used and breathing assessment done
    if not satsProbeUsed and breathing_assessed:
        print(25)  # UseSatsProbe
        s discrimptsatseProbeUsed = True
        continue

    # Manage Breathing insufficiency
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Disability check
    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Lastly, exposure check
    if not exposure_checked and disability_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        initial_assessments_done = True
        continue

    # Initiate BP check with cuff if not done
    if not bpCuffUsed and initial_assessments_done:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    # If BP is critically low (under 60 and measurable), get a reading
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Finish if conditions met
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

    # Default action if nothing else to be done
    print(0)  # DoNothing as last resort

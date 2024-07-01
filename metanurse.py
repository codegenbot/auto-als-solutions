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

    # Check for immediate life-threatening issues first
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Sats Probe needs to be used and it hasn't been used yet
    if not satsProbeUsed and (measured_times[5] == 0 or measured_values[5] < 88):
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # Regular assessments
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
                airway_confirmed = True
                if events[4] > 0.1 or events[5] > 0.1:  # Vomit or Blood in Airway
                    print(31)  # UseYankeurSuctionCatheter
                    continue
                else:
                    print(0)  # DoNothing (Airway is clear)
                    continue
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Provide additional oxygen if Sats below 88%
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check and manage blood pressure if needed
    if measured_times[4] == 0 or (measured_times[4] > 0 and measured_values[4] < 60):
        print(27)  # UseBloodPressureCuff
        continue

    # Stabilize the patient with all criteria met
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

    # Default action if nothing else is required
    print(0)  # DoNothing
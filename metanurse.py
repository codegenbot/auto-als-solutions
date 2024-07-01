airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
sats_probe_used = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check immediate critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
                airway_confirmed = True
                if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
                    print(31)  # UseYankeurSuctionCatheter
                    continue
                print(0)
                continue
            print(3)  # ExamineAirway
            continue

        if not breathing_assessed:
            if events[8] > 0 or events[7] > 0:
                breathing_assessed = True
                print(0)
                continue
            print(4)  # ExamineBreathing
            continue

        if not circulation_checked:
            if events[16] > 0 or events[17] > 0:
                circulation_checked = True
                print(0)
                continue
            print(5)  # ExamineCirculation
            continue

        if not disability_checked:
            if events[21] > 0 or events[22] > 0 or events[23] > 0:
                disability_checked = True
                print(0)
                continue
            print(6)  # ExamineDisability
            continue

        if not exposure_checked:
            exposure_checked = True
            print(7)  # ExamineExposure
            continue

        initial_assessments_done = True

    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue

    # Check if he needs immediate help due to measured sats
    if measured_values[5] < 88:
        if not events[18]:
            print(19)  # OpenBreethyleneDrawer
            continue
        print(30)  # UseNonRebreatherMask
        continue

    # Check if breathing interventions were enough
    if (
        measured_values[5] >= 88
        and measured_values[6] >= 8
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing as last resort
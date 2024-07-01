airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
sats_probe_used = False
breathing_drawer_opened = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Ventilation support if no breathing observed
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Sequential ABCDE assessment
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.5:  # AirwayClear
                airway_confirmed = True
            elif events[4] > 0.5 or events[5] > 0.5:  # AirwayVomit, AirwayBlood
                print(31)  # UseYankeurSuctionCatheter
                continue
            else:
                print(3)  # ExamineAirway
                continue

        elif not breathing_assessed:
            if measured_times[6] > 0 and measured_values[6] < 8:
                print(29)  # UseBagValveMask
                continue
            else:
                print(4)  # ExamineBreathing
                breathing_assessed = True
                continue

        elif not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        elif not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        elif not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Ensuring proper use of Sats probe
    if not sats_probe_used:
        if not breathing_drawer_opened:
            print(19)  # OpenBreathingDrawer
            breathing_drawer_opened = True
        else:
            print(25)  # UseSatsProbe
            sats_probe_used = True
        continue

    # Check if patient is stabilized
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

    # Minimum action if no critical situations
    print(0)  # DoNothing
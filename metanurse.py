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

    # Check immediate critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if events[7] > 0.5:  # BreathingNone - immediate action
        print(29)  # UseBagValveMask
        continue

    if not breathing_drawer_opened:
        print(19)  # OpenBreathingDrawer
        breathing_drawer_opened = True
        continue

    if not sats_probe_used and breathing_drawer_opened:
        print(25)  # UseSatsProbe
        sats_probe_used = True
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
                airway_confirmed = True
                if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
                    print(31)  # UseYankeurSuctionCatheter
                    continue
                print(0)  # DoNothing
                continue
            print(3)  # ExamineAirway
            continue

        if not breathing_assessed and measured_times[6] == 0:
            print(4)  # ExamineBreathing
            continue
        else:
            breathing_assessed = True

        if not circulation_checked and (events[16] == 0 and events[17] == 0):
            print(5)  # ExamineCirculation
            continue
        else:
            circulation_checked = True

        if not disability_checked and (
            events[21] == 0 and events[22] == 0 and events[23] == 0
        ):
            print(6)  # ExamineDisability
            continue
        else:
            disability_checked = True

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

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

    print(0)  # DoNothing as last resort
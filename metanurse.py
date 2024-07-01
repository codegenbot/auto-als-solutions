airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
sats_checked = False
sats_probe_used = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Start using the sats probe if not done to gather essential data
    if not sats_checked:
        if measured_times[5] == 0:
            print(25)  # UseSatsProbe
            continue
        else:
            sats_checked = True

    # If sats measured, view monitor
    if measured_times[5] > 0:
        sats = measured_values[5]
        if sats < 65:
            print(17)  # StartChestCompression
            continue
        elif sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

    # Airway assessment
    if not airway_confirmed:
        if (
            events[3] > 0.5 or events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5
        ):  # Airway issues
            print(36)  # PerformHeadTiltChinLift
            airway_confirmed = True
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing assessment
    if not breathing_assessed:
        if (
            events[7] > 0.5 or events[8] > 0.5 or events[9] > 0.5
        ):  # Breathing issues like None, Snoring, SeeSaw
            print(29)  # UseBagValveMask
            airway_confirmed = (
                True  # Ensures airway management in case of breathing issue
            )
            breathing_assessed = True
            continue
        else:
            print(4)  # ExamineBreathing
            continue

    # Circulation assessment
    if not circulation_checked:
        if events[16] > 0.5 or events[17] > 0.5:  # Circulation issues
            print(20)  # OpenCirculationDrawer
            circulation_checked = True
            continue
        else:
            print(5)  # ExamineCirculation
            continue

    # Check to finish if all health indicators are stabilized
    if (
        all([airway_confirmed, breathing_assessed, circulation_checked, sats_checked])
        and sats >= 88
    ):
        print(48)  # Finish
        break

    # If no specific actions are applicable, continue checking as per operations
    print(0)  # DoNothing
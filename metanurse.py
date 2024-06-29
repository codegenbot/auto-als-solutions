airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
breathingDrawerOpened = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:  # AirwayClear event present
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue
        elif not breathing_assessed:
            if events[10] > 0:  # BreathingEqualChestExpansion event present
                breathing_assessed = True
            else:
                if not breathingDrawerOpened:
                    print(19)  # OpenBreathingDrawer
                    breathingDrawerOpened = True
                    continue
                elif not satsProbeUsed:
                    print(25)  # UseSatsProbe
                    satsProbeUsed = True
                    continue
                else:
                    print(4)  # ExamineBreathing
                    continue
        elif not circulation_checked:
            if (
                events[16] > 0 or events[17] > 0
            ):  # RadialPulsePalpable or RadialPulseNonPalpable
                circulation_checked = True
            else:
                print(5)  # ExamineCirculation
                continue
        elif not disability_checked:
            if events[21] > 0 or events[22] > 0:  # AVPU_A or AVPU_U
                disability_checked = True
            else:
                print(6)  # ExamineDisability
                continue
        elif not exposure_checked:
            exposure_checked = True
            print(7)  # ExamineExposure
            continue
        else:
            initial_assessments_done = True

    # Sufficient stabilization criteria met?
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

    # If SATS or MAP haven't been measured or are below threshold, handle accordingly
    if not measured_times[5] or measured_values[5] < 88:
        if not satsProbeUsed:
            if not breathingDrawerOpened:
                print(19)  # OpenBreathingDrawer
                breathingDrawerOpened = True
            else:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
            continue
        else:
            print(16)  # ViewMonitor
    elif not measured_times[4] or measured_values[4] < 60:
        print(26)  # UseAline
        continue
    else:
        print(16)  # ViewMonitor
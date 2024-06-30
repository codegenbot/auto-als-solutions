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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:  # AirwayClear is significantly recent
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue

        if not breathing_assessed:
            if (
                measured_times[6] > 0 and measured_values[6] < 8
            ):  # Respiratory Rate too low
                print(29)  # UseBagValveMask
                continue
            if events[12] > 0 or events[13] > 0 or events[14] > 0:
                breathing_assessed = True
            print(4)  # ExamineBreathing
            continue

        if not circulation_checked:
            # Check RadialPulsePalpable and RadialPulseNonPalpable
            if events[16] > 0 or events[17] > 0:
                circulation_checked = True
            print(5)  # ExamineCirculation
            continue

        if not disability_checked:
            if (
                events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1
            ):  # AVPU responses
                disability_checked = True
            print(6)  # ExamineDisability
            continue

        if not exposure_checked:
            if events[26] > 0:  # Exposure indications noted
                exposure_checked = True
            print(7)  # ExamineExposure
            continue

        initial_assessments_done = True

    if initial_assessments_done:
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

        if not sats_probe_used:
            print(19)  # OpenBreathingDrawer
            print(25)  # UseSatsProbe
            sats_probe_used = True
            continue

        print(16)  # ViewMonitor
        continue
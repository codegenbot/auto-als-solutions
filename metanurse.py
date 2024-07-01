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

    # Immediate critical condition checks
    sats_index_time, sats_index_value, map_index_time, map_index_value = 40, 46, 44, 50
    if (
        measured_times[sats_index_time - 39] > 0
        and measured_values[sats_index_value - 46] < 65
    ) or (
        measured_times[map_index_time - 39] > 0
        and measured_values[map_index_value - 46] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        # Collect assessments in correct order if any are not confirmed
        if not airway_confirmed:
            print(3)  # ExamineAirway
            continue
        if not breathing_assessed:
            print(4)  # ExamineBreathing
            continue
        if not circulation_checked:
            print(5)  # ExamineCirculation
            continue
        if not disability_checked:
            print(6)  # ExamineDisability
            continue
        if not exposure_checked:
            print(7)  # ExamineExposure
            continue
        initial_assessments_done = True

    # Assessment results processing
    if not airway_confirmed and (
        events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0
    ):
        airway_confirmed = True
        if events[4] > 0.5 or events[5] > 0.5:  # Airway complications requiring suction
            print(31)  # UseYankeurSuctionCatheter
            continue

    if not breathing_assessed and (events[8] > 0.5 or events[7] > 0.5):
        breathing_assessed = True

    if not circulation_checked and (events[16] > 0.5 or events[17] > 0.5):
        circulation_checked = True

    if not disability_checked and (
        events[21] > 0.5 or events[22] > 0.5 or events[23] > 0.5
    ):
        disability_checked = True

    if not exposure_checked:
        exposure_checked = True

    # Reassess if needed based on new info
    if measured_times[sats_index_time - 39] > 0 and not sats_probe_used:
        # Check if breathing drawer needs to be opened to access Sats probe
        if not breathing_drawer_opened:
            print(19)  # OpenBreathingDrawer
            breathing_drawer_opened = True
            continue
        print(25)  # UseSatsProbe
        sats_probe_used = True
        continue

    # Check if conditions to finish are met
    if (
        sats_probe_used
        and measured_times[sats_index_time - 39] > 0
        and measured_values[sats_index_value - 46] >= 88
        and measured_times[42 - 39] > 0
        and measured_values[48 - 46] >= 8
        and measured_times[map_index_time - 39] > 0
        and measured_values[map_index_value - 46] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing as last resort
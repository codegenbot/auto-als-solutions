steps = 0
airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessment_done = False
sats_probe_used = False
bp_cuff_used = False

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical conditions management
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway Management
    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear
            airway_confirmed = True
            print(0)  # DoNothing
            continue
        elif events[4] > 0:  # AirwayVomit
            print(31)  # UseYankeurSuctionCatheter
            continue
        elif events[5] > 0 or events[6] > 0:  # AirwayBlood or AirwayTongue
            print(32)  # UseGuedelAirway
            continue
        print(3)  # ExamineAirway
        continue

    # Breathing management
    if not breathing_assessed:
        if events[7] > 0:  # BreathingNone
            print(29)  # UseBagValveMask
            continue
        if events[10] > 0:  # BreathingEqualChestExpansion
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    # Circulation management
    if not circulation_checked:
        if events[16] > 0:  # RadialPulsePalpable
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    # Disability management
    if not disability_checked:
        if events[21] > 0 or events[22] > 0:  # AVPU_V or AVPU_U
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    # Exposure management
    if not exposure_checked:
        exposure_checked = True
        print(7)  # ExamineExposure
        continue

    # Monitoring and measurements
    if not sats_probe_used:
        if measured_times[5] == 0:
            print(25)  # UseSatsProbe
            sats_probe_used = True
            continue

    if not bp_cuff_used:
        if measured_times[4] == 0:
            print(27)  # UseBloodPressureCuff
            bp_cuff_used = True
            continue

    # Check and conclude stabilisation
    if (
        measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[1] > 0
        and measured_values[1] >= 8
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing
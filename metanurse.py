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

    # Immediate actions based on vitals
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Initial ABCDE assessments
    if not initial_assessments_done:
        # Airway examination
        if not airway_confirmed:
            if (
                events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0
            ):  # Any bad airway sign
                airway_confirmed = True
                print(31)  # UseYankeurSuctionCatheter if needed
                continue
            print(3)  # ExamineAirway
            continue

        # Breathing examination
        if not breathing_assessed:
            if (
                events[8] > 0 or events[13] > 0 or events[14] > 0
            ):  # Breathing irregularity
                breathing_assessed = True
                print(0)  # DoNothing if breathing is somehow okay
                continue
            print(4)  # ExamineBreathing
            continue

        # Circulation examination
        if not circulation_checked:
            if events[16] > 0 or events[17] > 0:  # Radial pulse status
                circulation_checked = True
                print(0)  # DoNothing if circulation is somehow okay
                continue
            print(5)  # ExamineCirculation
            continue

        # Disability examination
        if not disability_checked:
            if events[21] > 0 or events[22] > 0 or events[23] > 0:  # AVPU status
                disability_checked = True
                print(0)  # DoNothing if disability is somehow okay
                continue
            print(6)  # ExamineDisability
            continue

        # Exposure examination
        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Active management steps
    # Use sats probe if not used or sats are unreliable
    if not satsProbeUsed and (measured_times[5] == 0 or measured_values[5] < 88):
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        print(16)  # ViewMonitor
        satsProbeUsed = True
        continue

    # Assess blood pressure if needed
    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    # Terminate if conditions are met
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
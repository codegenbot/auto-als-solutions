airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
monitorViewed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical responses
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    elif measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway handling
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0.1:  # AirwayClear
            airway_confirmed = True
        elif events[4] > 0.1 or events[5] > 0.1:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
        continue

    # Breathing assessments
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        if events[7] > 0.7:  # BreathingNone
            print(29)  # UseBagValveMask
        elif (
            events[8] > 0.1 or events[13] > 0.1 or events[14] > 0.1
        ):  # Breathing troubles
            breathing_assessed = True
        continue

    # Circulation check
    if not circulation_checked:
        print(5)  # ExamineCirculation
        if events[16] > 0.1:  # RadialPulsePalpable
            circulation_checked = True
        continue

    # Disability check
    if not disability_checked:
        print(6)  # ExamineDisability
        if events[21] > 0 or events[22] > 0 or events[23] > 0:  # AVPU responses
            disability_checked = True
        continue

    # Exposure check
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Monitor Sats
    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        continue

    if not monitorViewed:
        print(25)  # UseSatsProbe
        monitorViewed = True
        continue

    # Use non-rebreathing mask if sats are low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Use BP cuff if needed
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    # Stabilize patient and finish if all parameters are within normal limits
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing as a default action
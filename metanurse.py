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

    # Emergency handling for severe conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway handling
    if not airway_confirmed:
        if events[3] > 0.1:  # AirwayClear
            airway_confirmed = True
        elif events[4] > 0.1 or events[5] > 0.1:  # AirwayVomit, AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing handling
    if not breathing_assessed:
        if events[7] > 0.1 or (
            measured_times[6] > 0 and measured_values[6] < 8
        ):  # BreathingNone or bad measured resp rate
            print(29)  # UseBagValveMask
            continue
        if measured_times[6] > 0:  # Resp rate recently measured
            breathing_assessed = True
        print(4)  # ExamineBreathing
        continue

    # Circulation handling
    if not circulation_checked:
        if (
            events[16] > 0.1 or events[17] > 0.1
        ):  # RadialPulsePalpable, RadialPulseNonPalpable
            circulation_checked = True
        print(5)  # ExamineCirculation
        continue

    # Disability handling
    if not disability_checked:
        if events[21] > 0 or events[22] > 0 or events[23] > 0:  # AVPU_A, AVPU_V, AVPU_U
            disability_checked = True
        print(6)  # ExamineDisability
        continue

    # Exposure handling
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Confirm initial assessments are done
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_checked
    ):
        initial_assessments_done = True

    # Use sats probe if needed
    if not satsProbeUsed and measured_times[5] == 0:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # Maintaining Breath and MAP
    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        print(38)  # TakeBloodPressure
        continue

    # Finish if stabilized
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

    # Do nothing as a fallback
    if initial_assessments_done:
        print(0)  # DoNothing
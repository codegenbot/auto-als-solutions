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

    # Emergency conditions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check assessments
    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if airway_confirmed and not breathing_assessed:
        if any(events[8:15]):  # Any breathing-related event is observed
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    if airway_confirmed and breathing_assessed and not circulation_checked:
        if (
            events[16] > 0 or events[17] > 0
        ):  # RadialPulsePalpable or RadialPulseNonPalpable
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and not disability_checked
    ):
        if events[21] > 0 or events[22] > 0 or events[23] > 0:  # AVPU responses
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and not exposure_checked
    ):
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Stabilisation criteria check
    if exposure_checked:
        stable = (
            measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        )
        if stable:
            print(48)  # Finish
            break

        if not satsProbeUsed and (measured_times[5] == 0 or measured_values[5] < 88):
            print(19)  # OpenBreathingDrawer
            continue

        if measured_times[4] == 0 or measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            continue

        if measured_times[5] == 0 or measured_values[5] < 88:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue

        print(16)  # ViewMonitor
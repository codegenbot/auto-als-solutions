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

    if events[3] > 0.7:  # AirwayClear
        airway_confirmed = True

    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if airway_confirmed and not breathing_assessed:
        if events[6] > 0.7:  # BreathingNone
            if not satsProbeUsed:
                print(25)  # UseSatsProbe
                satsProbeUsed = True
            print(29)  # UseBagValveMask
            breathing_assessed = True
            continue
        elif events[7] > 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
            print(29)  # UseBagValveMask
            breathing_assessed = True
            continue
        else:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

    if airway_confirmed and breathing_assessed and not circulation_checked:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
        else:
            print(27)  # UseBloodPressureCuff
        circulation_checked = True
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and not disability_checked
    ):
        print(6)  # ExamineDisability
        disability_checked = True
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

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and exposure_checked
    ):
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
        else:
            print(0)  # DoNothing
            continue
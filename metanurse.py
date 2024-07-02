airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
monitorViewed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-critical actions
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        if events[38] > 0:  # Heart Rhythm VF detected
            print(28)  # AttachDefibPads (first attach pads if not yet)
            continue
        print(17)  # StartChestCompression
        continue

    # Initial ABCDE Assessments
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    elif not airway_confirmed and events[3] > 0:  # AirwayClear
        airway_confirmed = True

    if airway_confirmed and not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if airway_confirmed and breathing_assessed and not circulation_checked:
        print(5)  # ExamineCirculation
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
        initial_assessments_done = True
        continue

    # Progressive Interventions
    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if initial_assessments_done and measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if initial_assessments_done and not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    # Check and monitor BP
    if initial_assessments_done and measured_times[4] > 0 and measured_values[4] < 60:
        if not monitorViewed and bpCuffUsed:
            print(16)  # ViewMonitor
            monitorViewed = True
        else:
            print(15)  # GiveFluids
        continue

    # Check for stabilization and finish if conditions meet
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
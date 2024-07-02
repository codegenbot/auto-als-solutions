steps = 0
airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening checks
    if (measured_times[4] > 0 and measured_values[4] < 20) or (measured_times[5] > 0 and measured_values[5] < 65):
        print(17)  # StartChestCompression
        continue

    # Stabilize breathing
    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # ABCDE method
    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0:
                airway_confirmed = True
            continue

        if airway_confirmed and not breathing_assessed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

        if breathing_assessed and not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if circulation_checked and not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if disability_checked and not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            initial_assessments_done = True
            continue

    # Non-Rebreather Mask if low sats
    if not satsProbeUsed and breathing_assessed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check blood pressure
    if not bpCuffUsed and circulation_checked:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(38)  # TakeBloodPressure
        continue

    # Final condition to end the scenario
    if (
        measured_times[4] > 0 and measured_values[4] >= 60 and
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    # Default action when nothing else applies
    print(0)  # DoNothing as last resort